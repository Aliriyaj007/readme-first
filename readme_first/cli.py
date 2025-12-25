# readme_first/cli.py
import argparse
import sys
from readme_first.analyzer import analyze_repo

HELP_DESCRIPTION = """
Readme-First: The First-Run Experience Linter
=============================================

This tool scans your repository documentation to ensure it is "runnable" 
for new users. It checks for critical missing information that causes 
developer friction.

It looks for:
  - Installation instructions
  - Usage/Run commands
  - Prerequisites
  - Example output
  - Documented config files (.env, requirements.txt, etc.)
"""

HELP_EPILOG = """
EXAMPLES
--------
  # Check the current directory
  readme-first .

  # Check a remote GitHub repository
  readme-first https://github.com/Aliriyaj007/readme-first

  # Check a GitHub Pages site (automatically finds the repo)
  readme-first https://aliriyaj007.github.io/DigitalDeft/

FAQ
---
  Q: Does this tool run my code?
  A: No. It only scans your README.md and file structure for patterns. 
     It is safe to run on any repository.

  Q: What is a "good" score?
  A: A score above 80 is considered developer-friendly. 
     A score below 50 means most users will likely fail to run your project.

  Q: How do I improve my score?
  A: The tool provides a "What You Should Add" section with auto-generated 
     Quick Start commands. Copy-paste those into your README!

  Q: Why does it say "User-hostile"?
  A: If a user has to guess how to install dependencies or run the project, 
     it is hostile. Explicit instructions remove this friction.

  Q: Who made this?
  A: Built with \u2764\ufe0f by Riyajul Ali (https://github.com/Aliriyaj007)

For full documentation, visit: https://github.com/Aliriyaj007/readme-first
"""

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

class RichArgumentParser(argparse.ArgumentParser):
    def print_help(self, file=None):
        console = Console()
        
        # Title / Header
        console.print(Panel("[bold white]readme-first[/bold white]: [italic]The First-Run Experience Linter[/italic]", style="blue", expand=False))
        console.print()
        
        # Description
        console.print(Markdown(self.description))
        console.print()
        
        # Usage
        # Get usage without "usage: " prefix
        usage = self.format_usage().replace("usage: ", "").strip()
        console.print(f"[bold yellow]USAGE[/bold yellow]\n  {usage}")
        console.print()
        
        # Arguments (Custom styling)
        console.print("[bold yellow]ARGUMENTS[/bold yellow]")
        console.print("  [bold cyan]path[/bold cyan]")
        console.print("      Local path (e.g. '.') or remote GitHub URL to analyze")
        console.print()
        
        # Options
        console.print("[bold yellow]OPTIONS[/bold yellow]")
        console.print("  [bold cyan]-h, --help[/bold cyan]")
        console.print("      Show this help message and exit")
        console.print()
        
        # Epilog
        if self.epilog:
            console.print(Markdown(self.epilog))

def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding='utf-8')
        
    parser = RichArgumentParser(
        prog="readme-first",
        description=HELP_DESCRIPTION,
        epilog=HELP_EPILOG,
    )
    parser.add_argument(
        "path",
        help="Local path (e.g. '.') or remote GitHub URL to analyze"
    )

    args = parser.parse_args()
    analyze_repo(args.path)

if __name__ == "__main__":
    main()
