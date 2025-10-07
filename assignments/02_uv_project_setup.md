# Assignment 02 — UV Project Setup: Simple & Packaged Applications

Build two small Python apps using uv: one Simple Application and one Packaged Application. Both apps must implement any functionality you choose and print your Name and PIAIC Registration Number every time they run. Submit a GitHub link with screenshots in each app’s README.

## 🎯 Objectives

- Practice uv workflows for both simple and packaged apps
- Understand src layout, scripts, and running via `uv run`
- Capture evidence via terminal screenshots and README docs
- Push a clean, Python-ready repo with proper `.gitignore`

## ✅ Learning Outcomes

By the end, you’ll be able to:
- Initialize projects with `uv init` and `uv init --package`
- Structure code for simple vs. packaged apps
- Define and run CLI script entries in `pyproject.toml`
- Reproduce environments with `uv sync` and run code with `uv run`

## 📦 What you will create

A parent directory containing two uv projects:

```
uv-assignment/
├─ simple-app/              # uv simple application
│  ├─ main.py
│  ├─ pyproject.toml
│  ├─ README.md             # must include terminal screenshot
│  └─ .venv/ (auto, do not commit)
└─ packaged-app/            # uv packaged application (src layout)
   ├─ pyproject.toml
   ├─ README.md             # must include terminal screenshot
   └─ src/
      └─ my_packaged_app/
         ├─ __init__.py
         └─ main.py
```

At repo root (parent of both projects), include a Python-focused `.gitignore` to keep the repo clean.

## 📤 Submission

- Push your assignment to GitHub as a single repository containing both projects under one parent directory.
- Each project must include its own `README.md` with a terminal screenshot of the output.
- Submit the GitHub repository link.

## ✅ Deliverables Checklist

- Parent directory with two projects: `simple-app/` and `packaged-app/`
- Simple app prints your Name and PIAIC Reg# and implements some functionality
- Packaged app prints your Name and PIAIC Reg# and implements some functionality
- `README.md` in each project includes a terminal screenshot of the output
- Root-level `.gitignore` suitable for Python projects
- GitHub link submitted

## 🧪 Acceptance Criteria (Grading Rubric)

- Project structure (simple + packaged, uv usage): 20%
- Functionality present in both apps: 20%
- Required prints (Name + PIAIC Reg#) in both apps: 20%
- Documentation: readme + screenshot for each app: 25%
- Clean repo hygiene: `.gitignore`, no venv/build artifacts committed: 10%
- Commit history clarity (meaningful messages): 5%

Total: 100%

## 💡 Tips & Troubleshooting

- After editing `pyproject.toml`, run `uv sync` if dependencies or scripts changed.
- Use `uv run <command>` to execute within the project environment without activating the venv.
- If module imports fail when running by path, switch to script (`uv run packaged-app`) or module form (`uv run -m my_packaged_app.main`).
- Pin interpreter if required for your environment: `uv python pin 3.12`.

## 📚 References

- Class materials: `class02_20250824/01_uv/` (Simple and Packaged app READMEs)
- Official docs: https://docs.astral.sh/uv/
- Scripts guide: https://docs.astral.sh/uv/guides/scripts/
- Projects guide: https://docs.astral.sh/uv/guides/projects/
