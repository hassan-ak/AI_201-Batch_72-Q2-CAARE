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
    
    # Optional: PostgreSQL connection string (for SQLAlchemy session demo)
    postgresql_url: str | None = os.getenv("POSTGRESQL_URL")
    
    @classmethod
    def get_postgresql_async_url(cls) -> tuple[str | None, dict]:
        """
        Convert PostgreSQL URL to async format and extract SSL parameters.
        
        Converts: postgresql://user:pass@host/db?sslmode=require
        To: postgresql+asyncpg://user:pass@host/db (with SSL in connect_args)
        
        Returns:
            Tuple of (async_url, connect_args_dict)
        """
        url = cls.postgresql_url
        if not url:
            return None, {}
        
        # Parse URL to separate base URL and query parameters
        if "?" in url:
            base_url, query_string = url.split("?", 1)
        else:
            base_url = url
            query_string = ""
        
        # Parse query parameters
        from urllib.parse import parse_qs, urlencode
        
        connect_args = {}
        
        if query_string:
            params = parse_qs(query_string)
            
            # Handle sslmode parameter for asyncpg
            if "sslmode" in params:
                sslmode = params["sslmode"][0].lower()
                # asyncpg uses ssl='require' instead of sslmode=require
                if sslmode == "require" or sslmode == "prefer":
                    connect_args["ssl"] = "require"
                elif sslmode == "disable":
                    connect_args["ssl"] = False
                else:
                    connect_args["ssl"] = sslmode
                # Remove sslmode from params (we handle it separately)
                del params["sslmode"]
            
            # Handle channel_binding (asyncpg doesn't use this, but we can store it)
            if "channel_binding" in params:
                # asyncpg doesn't support channel_binding directly
                # It's typically handled automatically with SSL
                del params["channel_binding"]
            
            # Keep other parameters if needed
            # asyncpg-specific parameters can be added here
        
        # Replace postgresql:// with postgresql+asyncpg://
        if base_url.startswith("postgresql://"):
            async_url = base_url.replace("postgresql://", "postgresql+asyncpg://", 1)
        elif "postgresql+asyncpg://" in base_url:
            async_url = base_url
        else:
            async_url = base_url
        
        return async_url, connect_args