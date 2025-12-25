# readme_first/analyzer.py
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import urlparse
from rich.console import Console
from readme_first.checks import (
    find_readme,
    extract_readme_text,
    detect_repo_files,
    check_readme_sections
)
from readme_first.scorer import score_repo

console = Console()

def is_url(path_str: str) -> bool:
    try:
        result = urlparse(path_str)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def normalize_url(url: str) -> str:
    """Convert github.io URLs to github.com repo URLs."""
    parsed = urlparse(url)
    if not parsed.netloc.endswith("github.io"):
        return url
    
    # format: <user>.github.io/<repo> -> github.com/<user>/<repo>
    user = parsed.netloc.split(".")[0]
    path_parts = parsed.path.strip("/").split("/")
    
    if len(path_parts) >= 1:
        repo = path_parts[0]
        return f"https://github.com/{user}/{repo}"
    
    return url

def analyze_local_path(path: Path, repo_name: str = None):
    if not path.exists():
        console.print(f"[red]Path does not exist: {path}[/red]")
        return
        
    if not repo_name:
        repo_name = path.resolve().name

    readme_path = find_readme(path)
    repo_files = detect_repo_files(path)

    if not readme_path:
        score, report_data = score_repo(
            readme_text="",
            sections_found=set(),
            repo_files=repo_files,
            has_readme=False
        )
    else:
        text = extract_readme_text(readme_path)
        sections = check_readme_sections(text)
        score, report_data = score_repo(
            readme_text=text,
            sections_found=sections,
            repo_files=repo_files,
            has_readme=True
        )

    # UI Rendering
    console.print()
    console.rule("[bold]README-FIRST REPORT[/bold]")
    console.print()
    
    # 1. Repo Name
    console.print(f"Repository : [bold]{repo_name}[/bold]")
    
    # 2. Score & Status
    status_msg = ""
    status_color = ""
    if score < 50:
        status_msg = "❌  User-hostile"
        status_color = "red"
    elif score < 80:
        status_msg = "⚠️  Needs Work"
        status_color = "yellow"
    else:
        status_msg = "✅  Developer-friendly"
        status_color = "green"
        
    console.print(f"Readiness  : [{status_color}]{score} / 100   {status_msg}[/{status_color}]")
    console.print()

    # 3. Essentials
    if report_data["essentials"]:
        console.print("[bold red]❌ Missing Essentials[/bold red]")
        for item in report_data["essentials"]:
             console.print(f"[red]• {item}[/red]")
        console.print()

    # 4. Undocumented
    if report_data["undocumented"]:
        console.print("[bold yellow]⚠️ Detected but Undocumented[/bold yellow]")
        for item in report_data["undocumented"]:
             console.print(f"[yellow]• {item}[/yellow]")
        console.print()
        
    # 5. Quick Start
    from readme_first.generator import generate_quick_start
    quick_start_cmds = generate_quick_start(path)
    
    if quick_start_cmds:
        console.print("[bold green]✅ What You Should Add (Quick Start)[/bold green]")
        console.print()
        code_block = "\n".join(quick_start_cmds)
        # Using a simplistic indent for the block as per mockup
        for cmd in quick_start_cmds:
            console.print(f"    [white]{cmd}[/white]")
        console.print()

    console.print()
    console.rule()
    if score < 50:
        console.print("[dim]Tip: Repos scoring below 50 are usually abandoned by users.[/dim]")
    else:
         console.print("[dim]Tip: Keep up the good documentation![/dim]")
    
    console.print()
    console.print("[dim]Made by [link=https://github.com/Aliriyaj007]Aliriyaj007[/link] \u2764\ufe0f[/dim]", justify="right")
    console.print()

def analyze_repo(path_str: str):
    if is_url(path_str):
        repo_url = normalize_url(path_str)
        # Extract decent name 'user/repo'
        parsed = urlparse(repo_url)
        path = parsed.path.strip("/")
        repo_name = path if path else repo_url
        
        console.print(f"[blue]Cloning {repo_url}...[/blue]")
        
        temp_dir = tempfile.mkdtemp(prefix="readme_first_")
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", repo_url, temp_dir],
                check=True,
                capture_output=True
            )
            analyze_local_path(Path(temp_dir), repo_name=repo_name)
        except subprocess.CalledProcessError:
            console.print(f"[red]Failed to clone repository: {repo_url}[/red]")
        except Exception as e:
            console.print(f"[red]An error occurred: {e}[/red]")
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)
    else:
        analyze_local_path(Path(path_str))
