# readme_first/scorer.py

def score_repo(readme_text, sections_found, repo_files, has_readme):
    score = 100
    report_data = {
        "essentials": [],
        "undocumented": []
    }

    if not has_readme:
        return 0, {
            "essentials": ["No README file found"],
            "undocumented": []
        }

    if "installation" not in sections_found:
        score -= 15
        report_data["essentials"].append("Installation instructions")

    if "usage" not in sections_found:
        score -= 15
        report_data["essentials"].append("Run / usage command") # Changed text to match mockup

    if "example" not in sections_found:
        score -= 10
        report_data["essentials"].append("Example output")

    if "prerequisites" not in sections_found:
        score -= 10
        report_data["essentials"].append("Prerequisites/requirements section")

    if "requirements.txt" in repo_files and "requirements" not in readme_text:
        score -= 5
        report_data["undocumented"].append("requirements.txt")

    if ".env.example" in repo_files and "env" not in readme_text:
        score -= 5
        report_data["undocumented"].append(".env.example")
        
    # Additional checks could go here to catch other files if needed for "undocumented"
    # staying close to original logic for now, just split.

    return max(score, 0), report_data
