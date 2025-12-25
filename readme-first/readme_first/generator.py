# readme_first/generator.py
from pathlib import Path
import json

def generate_quick_start(repo_path: Path):
    commands = []
    
    # 1. Install
    if (repo_path / "requirements.txt").exists():
        commands.append("pip install -r requirements.txt")
    elif (repo_path / "pyproject.toml").exists():
        commands.append("pip install .")
    elif (repo_path / "package.json").exists():
        commands.append("npm install")
    elif (repo_path / "poetry.lock").exists():
        commands.append("poetry install")
        
    # 2. Environment
    if (repo_path / ".env.example").exists():
        commands.append("cp .env.example .env")
        
    # 3. Run
    if (repo_path / "docker-compose.yml").exists():
        commands.append("docker compose up")
    elif (repo_path / "package.json").exists():
        # Check for "dev" script
        try:
            pkg_json = json.loads((repo_path / "package.json").read_text(encoding="utf-8"))
            scripts = pkg_json.get("scripts", {})
            if "dev" in scripts:
                commands.append("npm run dev")
            elif "start" in scripts:
                 commands.append("npm start")
        except:
            pass
    elif (repo_path / "main.py").exists():
        commands.append("python main.py")
    elif (repo_path / "app.py").exists():
        commands.append("python app.py")
    elif (repo_path / "manage.py").exists():
        # Likely Django, but sticking to strict rules, maybe just run? 
        # User didn't specify manage.py rule, but hinted at it in reasoning.
        # User's strict table: main.py -> python main.py, app.py -> python app.py.
        # Checking user request again: "manage.py -> python manage.py runserver" was in *my* initial plan 
        # but user reply said "Run command rules... main.py, app.py".
        # I will stick to the user's explicit table to be safe, but can add manage.py if it's generic enough.
        # User RE-pasted the rules: main.py, app.py, docker-compose, npm run dev.
        # I will strictly follow that plus the "manage.py -> python manage.py runserver" from my thought process if reasonable,
        # but the prompt says "Decision Rules (IMPORTANT – Lock These)" and lists specific ones.
        # I will stick ONLY to the listed ones to avoid hallucination/guessing complaint.
        pass
        
    return commands
