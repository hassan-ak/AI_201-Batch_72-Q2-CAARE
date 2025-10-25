import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from typing import List
from dataclasses import dataclass

def _fail_missing(required: List[str]) -> None:
    console = Console()

    table = Table(show_header=False, box=None)
    table.add_column(style="bold red", no_wrap=True)
    table.add_column()

    for key in required:
        table.add_row("Missing:", f"[green]{key}[/green]")

    msg = (
        "Missing"
    )

    panel = Panel.fit(table, title="[bold red]Configuration Error[/bold red]", subtitle=msg)
    console.print(panel)
    raise SystemExit(1)


load_dotenv()

_required = [
    "GEMINI_API_KEY",
    "GEMINI_API_URL",
    "GEMINI_API_MODEL",
]

_missing = [k for k in _required if not os.getenv(k)]
if _missing:
    _fail_missing(_missing)

@dataclass
class Config:
    gemini_api_key: str = os.getenv(_required[0])
    gemini_api_url: str = os.getenv(_required[1])
    gemini_api_model: str = os.getenv(_required[2])