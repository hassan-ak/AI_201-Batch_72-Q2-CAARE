# Async Programming

## 1) Overview

A tiny demo that contrasts synchronous vs asynchronous I/O using a fake file downloader. It showcases:

- `async def` and `await`
- Running tasks concurrently with `asyncio.gather`
- Measuring elapsed time to see the speedup

This project pairs with the lesson in `../Readme.md` and provides a runnable example.

## 2) Prerequisites

- Python 3.13+ (matches `pyproject.toml`)
-  `uv` for environment and run commands

Check versions:

```bash
python --version
uv --version  # optional
```

## 3) Project structure

```
async-programming/
├── pyproject.toml
├── README.md
└── src/
	└── async_programming/
		├── __init__.py
		└── main.py
```

- `main.py` contains both sync and async implementations and small runners.
- `pyproject.toml` exposes three script entries for easy running.

## 4) Setup

From the `async-programming/` folder, create the environment and lock file:

```bash
uv sync
```

VS Code users: Select the interpreter from `.venv` if you want to run/debug without `uv run`.

## 5) Run the demo

Use the CLI scripts defined in `pyproject.toml` (recommended):

```bash
uv run run-sync     # runs the synchronous version
uv run run-async    # runs the asynchronous version
uv run run-module   # runs both (sync then async)
```

## 6) What each entry does

- `run-sync` → calls `async_programming.main:run_sync_main()`
- `run-async` → calls `async_programming.main:run_async_main()`
- `run-module` → runs both, back-to-back

## 7) Expected output

You’ll see each file’s start/finish and a final total time line. Sync runs take roughly the sum of delays; async runs take about as long as the slowest single task.

```
[SYNC] Starting sequential downloads...
Starting download: file1.zip
Finished downloading: file1.zip in 4 seconds
Starting download: file2.mp4
Finished downloading: file2.mp4 in 3 seconds
Starting download: file3.pdf
Finished downloading: file3.pdf in 5 seconds
Starting download: file4.jpg
Finished downloading: file4.jpg in 3 seconds
Starting download: file5.docx
Finished downloading: file5.docx in 2 seconds
[SYNC] All downloads finished in 17.00s


[ASYNC] Starting concurrent downloads...
Starting download: file1.zip
Starting download: file2.mp4
Starting download: file3.pdf
Starting download: file4.jpg
Starting download: file5.docx
Finished downloading: file3.pdf in 2 seconds
Finished downloading: file5.docx in 2 seconds
Finished downloading: file1.zip in 4 seconds
Finished downloading: file2.mp4 in 4 seconds
Finished downloading: file4.jpg in 4 seconds
[ASYNC] All downloads finished in 4.00s
```

## 8) How it works (quick notes)

- Sync path uses `time.sleep(...)` (blocking).
- Async path uses `await asyncio.sleep(...)` to yield control while waiting.
- `asyncio.gather(...)` runs the coroutines concurrently.
- `time.perf_counter()` measures wall-clock time.

`asyncio.sleep` simulates I/O waits; real apps would await network, DB, or file operations.

## 9) Troubleshooting

- "command not found: uv" → Install uv or use Python directly.
- "ModuleNotFoundError: async_programming" → Run with `uv run -m ...` or from the project root after `uv sync`.
- Long runs or varying times → Random delays (1–5s) are intentional to show differences.

## 10) Quick commands reference

```bash
# from async-programming/
uv sync
uv run run-sync
uv run run-async
uv run run-module
```