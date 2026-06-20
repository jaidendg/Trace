from core.base import Command
from core.registry import Registry
from cli.format import Format

from rich.console import Console
from rich.panel import Panel


class InfoCommand(Command):
    name = "info"
    description = "Show information about a module."
    aliases = []

    def __init__(self):
        self.registry = Registry()
        self.fmt = Format()
        self.console = Console()

    @Command.execute
    def run(self, module_name: str):
        module = self.registry.get_module(module_name)

        if not module:
            self.fmt.error(f"Module '{module_name}' not found.")
            return

        args = ", ".join(f"[bright_white]{arg}[/bright_white]" 
                         for arg in module.arguments())

        card_content = (
            f"[bold cyan]Arguments:[/bold cyan] {args}\n\n"
            f"[bold cyan]Description:[/bold cyan]\n[bright_white]{module.description}[/bright_white]"
        )

        self.console.print(
            Panel(
                card_content,
                title=f"✗ [bold cyan]{module.name}[/bold cyan]",
                title_align="left",
                border_style="bright_white",
                expand=False
            )
        )