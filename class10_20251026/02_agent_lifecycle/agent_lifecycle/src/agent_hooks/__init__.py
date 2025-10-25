# Agent Lifecycle Callbacks/Hooks
from agents import Agent, AgentHooks, RunContextWrapper, Tool, Usage
from typing import Any
from rich import print


class HelloAgentHooks(AgentHooks):
    def __init__(self, display_name: str):
        self.event_counter = 0
        self.display_name = display_name

    def _usage_to_str(self, usage: Usage) -> str:
        return f"{usage.requests} requests, {usage.input_tokens} input tokens, {usage.output_tokens} output tokens, {usage.total_tokens} total tokens"

    async def on_start(self, context: RunContextWrapper, agent: Agent) -> None:
        self.event_counter += 1
        print(
            f"[bright_green]Agent Hook[/bright_green] [bold cyan]### ({self.display_name}) {self.event_counter}:[/bold cyan] [green]Agent {agent.name} started.[/green] [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )

    async def on_handoff(
        self, context: RunContextWrapper, agent: Agent, source: Agent
    ) -> None:
        self.event_counter += 1
        print(
            f"[bright_green]Agent Hook[/bright_green] [bold cyan]### ({self.display_name}) {self.event_counter}:[/bold cyan] [orange1]Agent {source.name} handed off to {agent.name}.[/orange1] [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )

    async def on_tool_start(
        self, context: RunContextWrapper, agent: Agent, tool: Tool
    ) -> None:
        self.event_counter += 1
        print(
            f"[bright_green]Agent Hook[/bright_green] [bold cyan]### ({self.display_name}) {self.event_counter}:[/bold cyan] [blue]Agent {agent.name} started tool {tool.name}.[/blue] [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )

    async def on_tool_end(
        self, context: RunContextWrapper, agent: Agent, tool: Tool, result: str
    ) -> None:
        self.event_counter += 1
        print(
            f"[bright_green]Agent Hook[/bright_green] [bold cyan]### ({self.display_name}) {self.event_counter}:[/bold cyan] [blue]Agent {agent.name} ended tool {tool.name}[/blue] with result [magenta]{result}[/magenta]. [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )

    async def on_llm_start(
        self, context: RunContextWrapper, agent, system_prompt, input_items
    ):
        self.event_counter += 1
        print(
            f"[bright_green]Agent Hook[/bright_green] [bold cyan]### ({self.display_name}) {self.event_counter}:[/bold cyan] [deep_pink4]Agent {agent.name} started LLM call.[/deep_pink4] [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )

    async def on_llm_end(self, context, agent, response):
        self.event_counter += 1
        print(
            f"[bright_green]Agent Hook[/bright_green] [bold cyan]### ({self.display_name}) {self.event_counter}:[/bold cyan] [deep_pink4]Agent {agent.name} ended LLM call.[/deep_pink4] [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )

    async def on_end(
        self, context: RunContextWrapper, agent: Agent, output: Any
    ) -> None:
        self.event_counter += 1
        print(
            f"[bright_green]Agent Hook[/bright_green] [bold cyan]### ({self.display_name}) {self.event_counter}:[/bold cyan] [red]Agent {agent.name} ended[/red] with output [magenta]{output}[/magenta]. [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )
