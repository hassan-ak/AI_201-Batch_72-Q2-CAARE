import subprocess


def main() -> int:

    args = ["uv", "run", "chainlit", "run", "src/chatbot/app.py", "-w"]

    return subprocess.run(args).returncode