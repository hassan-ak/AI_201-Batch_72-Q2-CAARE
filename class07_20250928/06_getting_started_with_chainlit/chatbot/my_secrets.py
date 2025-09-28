import os
import rich
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_api_url = os.getenv("GEMINI_API_URL")
gemini_api_model = os.getenv("GEMINI_API_MODEL")

if not gemini_api_key:
    rich.print("[bold red]Error:[/bold red] [green]GEMINI_API_KEY[/green] is not set in the environment variables.")
    exit(1)
    
if not gemini_api_url:
    rich.print("[bold red]Error:[/bold red] [green]GEMINI_API_URL[/green] is not set in the environment variables.")
    exit(1)
    
if not gemini_api_model:
    rich.print("[bold red]Error:[/bold red] [green]GEMINI_API_MODEL[/green] is not set in the environment variables.")
    exit(1)
    
class Secrets:
    def __init__(self):
        self.gemini_api_key = gemini_api_key
        self.gemini_api_url = gemini_api_url
        self.gemini_api_model = gemini_api_model