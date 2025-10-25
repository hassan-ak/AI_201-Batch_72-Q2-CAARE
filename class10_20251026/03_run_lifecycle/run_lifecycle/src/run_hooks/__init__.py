from agents import RunHooks, RunContextWrapper, Agent, Tool, Usage, TContext, TResponseInputItem, ModelResponse
from typing import Optional
from typing import Any
from rich import print


class ExampleRunnerHooks(RunHooks):
    def __init__(self):
        self.event_counter = 0

    def _usage_to_str(self, usage: Usage) -> str:
        return f"{usage.requests} requests, {usage.input_tokens} input tokens, {usage.output_tokens} output tokens, {usage.total_tokens} total tokens"

    async def on_agent_start(self, context: RunContextWrapper, agent: Agent) -> None:
        self.event_counter += 1
        print(
            f"[bold cyan]### {self.event_counter}:[/bold cyan] [green]Agent {agent.name} started.[/green] [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )

    async def on_agent_end(
        self, context: RunContextWrapper, agent: Agent, output: Any
    ) -> None:
        self.event_counter += 1
        print(
            f"[bold cyan]### {self.event_counter}:[/bold cyan] [red]Agent {agent.name} ended[/red] with output [magenta]{output}[/magenta]. [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )

    async def on_tool_start(
        self, context: RunContextWrapper, agent: Agent, tool: Tool
    ) -> None:
        self.event_counter += 1
        print(
            f"[bold cyan]### {self.event_counter}:[/bold cyan] [blue]Tool {tool.name} started.[/blue] [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )

    async def on_tool_end(
        self, context: RunContextWrapper, agent: Agent, tool: Tool, result: str
    ) -> None:
        self.event_counter += 1
        print(
            f"[bold cyan]### {self.event_counter}:[/bold cyan] [blue]Tool {tool.name} ended[/blue] with result [magenta]{result}[/magenta]. [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )

    async def on_handoff(
        self, context: RunContextWrapper, from_agent: Agent, to_agent: Agent
    ) -> None:
        self.event_counter += 1
        print(
            f"[bold cyan]### {self.event_counter}:[/bold cyan] [orange1]Handoff from {from_agent.name} to {to_agent.name}.[/orange1] [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )

    async def on_llm_start(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent[TContext],
        system_prompt: Optional[str],
        input_items: list[TResponseInputItem],
    ) -> None:
        self.event_counter += 1
        print(
            f"[bold cyan]### {self.event_counter}:[/bold cyan] [deep_pink4]LLM Call started.[/deep_pink4] [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )

    async def on_llm_end(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent[TContext],
        response: ModelResponse,
    ) -> None:
        self.event_counter += 1
        print(
            f"[bold cyan]### {self.event_counter}:[/bold cyan] [deep_pink4]LLM Call ended.[/deep_pink4] [yellow]Usage: {self._usage_to_str(context.usage)}[/yellow]"
        )