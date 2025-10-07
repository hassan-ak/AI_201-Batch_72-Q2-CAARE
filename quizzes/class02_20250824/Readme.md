# Class 02 Mastery Quiz — `uv` (Projects, Environments, Scripts, Workflow)

A comprehensive multiple-choice quiz covering the `uv` module: overview, installation context, simple vs packaged apps, src layout, scripts, lifecycle, locking, running code, dev tools, groups, CI, build/publish, cache/offline, monorepos, and pitfalls.

Instructions: Choose the single best answer for each question. (Answers at the end.)

## Quiz

1. `uv` primarily manages Python projects using two key files:

   A. setup.cfg and requirements.txt  
   B. Pipfile and Pipfile.lock  
   C. pyproject.toml and uv.lock  
   D. package.json and package-lock.json

2. The role of `pyproject.toml` in `uv` is to:

   A. Store exact resolved versions only  
   B. Declare project metadata and requested dependencies  
   C. Cache wheels  
   D. Replace Python itself

3. The purpose of `uv.lock` is to:

   A. Ignore dev dependencies  
   B. Ensure reproducible installs by pinning exact versions  
   C. Replace virtual environments  
   D. Track only transitive dev tools

4. Command to initialize a new simple application:

   A. uv new my-app  
   B. uv init my-app  
   C. uv start my-app  
   D. uv create my-app

5. Command to initialize a packaged application using the `src` layout:

   A. uv init --package my-pkg  
   B. uv package init my-pkg  
   C. uv init-src my-pkg  
   D. uv pkg my-pkg

6. A key advantage of the `src` layout for packaged apps is:

   A. Faster top-level prints  
   B. Prevents accidental imports from local files during development  
   C. Eliminates need for `__init__.py`  
   D. Disables CLI script entries

7. To pin the Python interpreter version for a project:

   A. uv run python --pin 3.12  
   B. uv python pin 3.12  
   C. uv lock python 3.12  
   D. uv set python 3.12

8. The effect of `uv sync` is best described as:

   A. Deletes venv and lock file  
   B. Ensures environment matches the lock file, creating `.venv` and `uv.lock` as needed  
   C. Only formats code  
   D. Publishes to PyPI

9. Add a runtime dependency and install it in one atomic step:

   A. pip install <pkg>  
   B. uv add <pkg>  
   C. uv dep add <pkg> && pip install <pkg>  
   D. uv lock <pkg>

10. Add a development-only tool (e.g., linter) the `uv` way:

    A. uv add --dev ruff  
    B. uv dev add ruff  
    C. pip install ruff --dev  
    D. uv add ruff --tool

11. Install an optional feature group (e.g., docs):

    A. uv add --phase docs mkdocs  
    B. uv add --group docs mkdocs  
    C. uv group add mkdocs  
    D. uv extras docs mkdocs

12. Strictly reproduce the environment from the lock file without re-resolving:

    A. uv sync --frozen  
    B. uv lock --frozen  
    C. uv install --frozen  
    D. uv run --frozen

13. Run a command in the project environment without manually activating the venv:

    A. uv exec  
    B. uv run <cmd>  
    C. uv enter <cmd>  
    D. uv venv <cmd>

14. Run a Python module (package-aware) via `uv`:

    A. uv run -m my_package.main  
    B. uv run python -mm my_package.main  
    C. uv module run my_package.main  
    D. uv start -m my_package.main

15. CLI script entries are defined in which section of `pyproject.toml`?

    A. [tool.uv.scripts]  
    B. [project.scripts]  
    C. [cli.scripts]  
    D. [entrypoints]

16. The mapping format for a script entry is:

    A. command = "module:function"  
    B. command = "module#function"  
    C. command = "module.function"  
    D. command = "function:module"

17. In the packaged app example, why did the top-level print in `main.py` appear before `main()` output?

    A. CLI ignores functions  
    B. Top-level code runs immediately on import/execution before calling `main()`  
    C. uv reorders prints  
    D. Python buffers and reverses output

18. A common pitfall for newcomers using `uv` is:

    A. Committing `pyproject.toml`  
    B. Forgetting to commit `uv.lock`  
    C. Using `uv run`  
    D. Creating a venv

19. Why avoid mixing `pip install` with `uv add` in the same project?

    A. It slows down imports  
    B. It can desynchronize declared dependencies and the lock file  
    C. It removes `.venv`  
    D. It disables editor integration

20. If you hand-edit `pyproject.toml`, what must you do to refresh the lock?

    A. Reinstall Python  
    B. Run a command that re-locks, e.g., `uv sync`  
    C. Delete `uv.lock`  
    D. Nothing; it auto-updates instantly

21. Build distributable artifacts for your package:

    A. uv package  
    B. uv build  
    C. uv bundle  
    D. uv make

22. Publish your package to PyPI or another index:

    A. uv publish  
    B. uv upload  
    C. uv release  
    D. uv push

23. Clear old caches to free disk space:

    A. uv cache prune  
    B. uv cache clear-all  
    C. uv prune  
    D. uv clean-cache

24. Offline/restricted installs are enabled by:

    A. Only `pip`  
    B. Cache export/import plus `uv sync --frozen`  
    C. uv offline install  
    D. Disabling the lock

25. CI reproducibility recommendations include:

    A. uv sync --frozen in CI  
    B. Ignore `uv.lock` in CI  
    C. Use global Python only  
    D. Avoid `uv run`

26. Inspect environment packages for this project specifically:

    A. pip list  
    B. uv run pip list  
    C. uv list  
    D. uv packages

27. In a monorepo with multiple projects, each should have:

    A. One shared `uv.lock` at repo root  
    B. Its own `pyproject.toml` and `uv.lock` for independent syncing  
    C. No lock files  
    D. Only one `pyproject.toml` globally

28. Running a file path like `uv run python ./src/pkg/main.py` can fail because:

    A. uv forbids file runs  
    B. Path execution runs as `__main__` and breaks relative imports; prefer module/script runs  
    C. Python can’t load files  
    D. Top-level code is disallowed

29. In a simple application, exposing a script entry in `pyproject.toml` typically requires:

    A. [project.scripts] only  
    B. [project.scripts] plus `[tool.uv] package = true`  
    C. [tool.scripts] only  
    D. [entry.scripts] with `package = false`

30. When should you choose a packaged application over a simple application?

    A. For quick one-off scripts  
    B. For long-term, distributable apps with clean imports and CLI entries  
    C. For single-file throwaways  
    D. For local-only experiments

### Advanced Scenarios (Detailed MCQs)

31. You manually added `httpx` under `[project] dependencies` in `pyproject.toml` but didn’t run any command yet. `uv run python -c "import httpx"` fails. Next step?

    A. uv add httpx  
    B. uv sync  
    C. pip install httpx  
    D. uv build

32. In CI, `pyproject.toml` changed but `uv.lock` wasn’t updated locally. Which command ensures the pipeline fails to avoid drift?

    A. uv sync  
    B. uv sync --frozen  
    C. uv add --frozen  
    D. uv publish

33. You want to remove a dependency and keep the lock consistent. What should you run?

    A. pip uninstall <pkg>  
    B. uv remove <pkg>  
    C. Delete it from `pyproject.toml` only  
    D. uv prune <pkg>

34. Safest way to update all dependencies to newer compatible versions and refresh the lock:

    A. uv upgrade  
    B. uv add --upgrade  
    C. uv sync --upgrade  
    D. pip list --outdated

35. You defined a docs feature group. How do you install only that group for this environment?

    A. uv sync --group docs  
    B. uv add docs  
    C. uv run --group docs  
    D. uv lock --group docs

36. Best way to run a linter using versions pinned in the project lock file:

    A. Run linter installed globally  
    B. uv run ruff  
    C. pipx run ruff  
    D. uv exec ruff --global

37. In a simple app, you added `[project.scripts] myapp = "main:main"`, but `uv run myapp` says command not found. Likely missing step?

    A. Add `[tool.uv] package = true` and run `uv sync`  
    B. Move to `src/` layout  
    C. Rename `main.py` to `__main__.py`  
    D. Run `pip install -e .`

38. Where should you set the minimum required Python version for the project?

    A. `[project] requires-python`  
    B. `[tool.uv] requires-python`  
    C. `uv.lock`  
    D. `.venv/python-version`

39. In VS Code, to use the `uv` project interpreter directly, select:

    A. System Python  
    B. `.venv/bin/python` (or Windows: `.venv\\Scripts\\python.exe`)  
    C. Any interpreter in PATH  
    D. `uv.lock`

40. After defining `[project.scripts]`, when are CLI commands available?

    A. Only after global install  
    B. Immediately via `uv run <command>` once synced  
    C. Only with `python -m`  
    D. Only in packaged apps published to PyPI

41. You run `uv publish` without running `uv build` first. What happens?

    A. It fails because artifacts are missing  
    B. It builds if needed and uploads  
    C. It deletes the environment  
    D. It only tags the repo

42. Why prefer `uv run pytest`?

    A. Uses global pytest installation  
    B. Ensures tests run inside the project environment with locked versions  
    C. Skips the environment  
    D. Disables plugins by default

43. In a monorepo, from Project A you try `uv run -m project_b.main` and it fails. Reason?

    A. uv can’t work in monorepos  
    B. Each project has its own env/module path; run from Project B or configure appropriately  
    C. You must enable monorepo mode  
    D. You need `pip install -e ..`

44. When will `uv sync --frozen` error out?

    A. When lock and manifest differ  
    B. When cache is missing  
    C. When `.venv` already exists  
    D. When there’s no internet, unconditionally

45. Which best describes `uv upgrade`?

    A. Re-resolves, locks, and installs updated dependency versions  
    B. Clears the lock file  
    C. Only updates dev dependencies  
    D. Only upgrades Python

46. Migration support described in notes means `uv` can:

    A. Import from legacy requirement files and converge to `pyproject.toml` + `uv.lock`  
    B. Only work with new projects  
    C. Replace Git history  
    D. Eliminate lock files completely

47. Minimum files to commit for reproducible environments:

    A. Only `uv.lock`  
    B. Only `pyproject.toml`  
    C. `pyproject.toml` and `uv.lock`  
    D. `.venv`

48. In a simple app with `main.py` at project root, which run is correct for module-style execution?

    A. uv run myapp  
    B. uv run -m my_simple_app.main  
    C. uv run -m main  
    D. uv run python src/main.py

49. Recommended placement of most application logic in a packaged app:

    A. Heavy `__init__.py`  
    B. Put logic in `main.py` (keep `__init__` light)  
    C. Only top-level prints  
    D. Outside `src/`

50. You see `ModuleNotFoundError` when running `uv run python ./src/my_packaged_app/main.py` due to relative imports. Fix?

    A. Use `uv run -m my_packaged_app.main`  
    B. Use `pip install .`  
    C. Remove relative imports  
    D. Add sys.path hacks

## Answer Key

|   Q | A   |   Q | A   |   Q | A   |   Q | A   |   Q | A   |   Q | A   |
| --: | :-- | --: | :-- | --: | :-- | --: | :-- | --: | :-- | --: | :-- |
|   1 | C   |   2 | B   |   3 | B   |   4 | B   |   5 | A   |   6 | B   |
|   7 | B   |   8 | B   |   9 | B   |  10 | A   |  11 | B   |  12 | A   |
|  13 | B   |  14 | A   |  15 | B   |  16 | A   |  17 | B   |  18 | B   |
|  19 | B   |  20 | B   |  21 | B   |  22 | A   |  23 | A   |  24 | B   |
|  25 | A   |  26 | B   |  27 | B   |  28 | B   |  29 | B   |  30 | B   |
|  31 | B   |  32 | B   |  33 | B   |  34 | A   |  35 | A   |  36 | B   |
|  37 | A   |  38 | A   |  39 | B   |  40 | B   |  41 | B   |  42 | B   |
|  43 | B   |  44 | A   |  45 | A   |  46 | A   |  47 | C   |  48 | C   |
|  49 | B   |  50 | A   |     |     |     |     |     |     |     |     |

## Topic Coverage Map

- Q1–3: Core files and roles (pyproject.toml, uv.lock)
- Q4–6: Init flows and `src` layout rationale
- Q7–9: Python pinning, sync semantics, adding dependencies
- Q10–12: Dev tools, groups, strict frozen sync
- Q13–16: Running code (uv run, -m), defining scripts
- Q17–20: Top-level code behavior, pitfalls, lock refresh
- Q21–22: Build and publish lifecycle
- Q23–24: Cache management and offline installs
- Q25–27: CI reproducibility and monorepo practices
- Q28–30: Module vs path execution, simple vs packaged app choices
- Q31–34: Manual edits vs sync, CI frozen sync, remove/upgrade flows
- Q35–36: Optional groups, dev tools via uv run
- Q37–40: Simple app script exposure, requires-python, selecting interpreter, CLI availability
- Q41–42: Publish behavior, running tests with locked env
- Q43–44: Monorepo environment separation, frozen mismatch failures
- Q45–47: Upgrade semantics, migration support, files to commit
- Q48–50: Module-style runs for simple/packaged apps, relative import fixes
