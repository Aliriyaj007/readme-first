# readme_first/checks.py
from pathlib import Path
import re

REQUIRED_SECTIONS = {
    "installation": ["install", "setup"],
    "usage": ["usage", "run"],
    "prerequisites": ["requirements", "prerequisites"],
    "example": ["example", "output", "demo"],
}

def find_readme(repo_path: Path):
    for name in ["README.md", "README.rst", "README.txt"]:
        path = repo_path / name
        if path.exists():
            return path
    return None

def extract_readme_text(readme_path: Path) -> str:
    return readme_path.read_text(encoding="utf-8", errors="ignore").lower()

def check_readme_sections(text: str):
    found = set()
    for section, keywords in REQUIRED_SECTIONS.items():
        for kw in keywords:
            if re.search(rf"\b{kw}\b", text):
                found.add(section)
                break
    return found

def detect_repo_files(repo_path: Path):
    files = set()
    for f in [
        "requirements.txt",
        "pyproject.toml",
        "package.json",
        ".env.example",
        "docker-compose.yml"
    ]:
        if (repo_path / f).exists():
            files.add(f)
    return files
