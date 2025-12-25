# readme-first

A CLI utility that checks if a GitHub repository is "first-run friendly" and helps developers lower the barrier to entry.

## 🧐 Why This Exists

We've all been there: you find an interesting open-source project, clone it, and then... nothing.
- No installation instructions.
- No `pip install` or `npm install` command.
- No "how to run" section.
- Just a list of files and frustration.

Most developers write code first and documentation last (or never). This friction kills adoption. If a user can't run your project in < 60 seconds, they will leave.

**This tool exists because open-source projects should be runnable, not just readable.**

## 🛠️ What It Does

`readme-first` acts as a linter for "runnability". It:
-   **Scans** your local folder or a remote GitHub URL.
-   **Scores** the repository (0-100) based on documentation completeness.
-   **Detects** missing essential sections (Installation, Usage, Prerequisites).
-   **Identifies** undocumented configuration files (e.g., hidden `requirements.txt` or `.env.example`).
-   **Generates** a "Quick Start" snippet you can copy-paste directly into your README.

It does **not** critique your code style, architecture, or grammar. It only cares about one thing: **Can a stranger run this?**

## 🔄 Before / After

### Before
Manual investigation required:
- *Open `pyproject.toml`... okay, it uses poetry?*
- *Check `package.json`... there is a `dev` script.*
- *Try running it... error: missing environment variable.*
- *Give up.*

### After
Run one command:
```bash
readme-first https://github.com/user/project
```

Get immediate, actionable feedback:
```text
Readiness  : 42 / 100   ❌  User-hostile

❌ Missing Essentials
• Installation instructions
• Run / usage command

✅ What You Should Add (Quick Start)
    pip install -r requirements.txt
    cp .env.example .env
    python main.py
```

## 📸 Sample Output

```text
───────────────────────────── README-FIRST REPORT ─────────────────────────────

Repository : aliriyaj007/DigitalDeft
Readiness  : 75 / 100   ⚠️  Needs Work

❌ Missing Essentials
• Installation instructions
• Prerequisites/requirements section


───────────────────────────────────────────────────────────────────────────────
Tip: Keep up the good documentation!

                                                          Made by Aliriyaj007 ❤️
```

## 📦 Installation

### Option 1: Using pipx (Recommended)
`pipx` installs the tool in an isolated environment, keeping your system Python clean.

```bash
pipx install readme-first
```

### Option 2: Using pip
Install directly into your current Python environment (or specific venv).

```bash
pip install readme-first
```

### Option 3: From Source
For contributors or those who want the bleeding edge.

```bash
git clone https://github.com/Aliriyaj007/readme-first.git
cd readme-first
pip install -e .
```

## 🚀 Usage

### Local Repository
Navigate to your project directory and run:

```bash
readme-first .
```

### Remote Repository
Check any public GitHub repository directly:

```bash
readme-first https://github.com/Aliriyaj007/readme-first
```

### Help
See all available options:

```bash
readme-first --help
```

## 💡 How Scoring Works

The tool starts with a score of **100** and deducts points for friction:
- **-15**: Missing Installation instructions.
- **-15**: Missing Usage/Run instructions.
- **-10**: Missing Prerequisites section.
- **-10**: Missing Example output/demo.
- **-5**: Undocumented `requirements.txt` / `package.json`.
- **-5**: Undocumented `.env.example`.

**< 50**: Usually abandoned or experimental.
**> 80**: Developer-friendly.

## 🛣️ Roadmap

- [x] Local directory scanning
- [x] Remote GitHub URL scanning (`git clone` support)
- [x] `github.io` page URL resolution
- [x] Auto-generated "Quick Start" block
- [x] Professional CLI output (Rich/Color)
- [ ] CI/CD Action integration (block PRs on low readability score)
- [ ] Support for `GO`, `Rust`, and `Java` build systems
- [ ] Customizable scoring rules (`.readmerc`)

## ⚠️ Limitations

- The tool relies on keyword matching (regex) in the README. It is heuristic, not semantic. It might miss instructions written in unusual ways.
- It assumes standard file names (`README.md`, `README.txt`, `README.rst`).
- It does not actually *run* your code to verify it works (that would be unsafe).

## 🤝 Contributing

Contributions are welcome!
1.  Fork the repo.
2.  Create a feature branch.
3.  Submit a PR with a clear description.

*Please ensure your code passes linting and includes relevant tests.*

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

## 👨‍💻 Author

**Riyajul Ali**

- **GitHub**: [Aliriyaj007](https://github.com/Aliriyaj007)
- **Email**: aliriyaj007@protonmail.com

*"Built to remove friction, not add features."*
