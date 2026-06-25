from core.base import Command
from core.registry import Registry
from cli.format import Format

from rich.console import Console
from rich.panel import Panel


class InfoCommand(Command):
    name = "info"
    description = "Show information about a module."

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

        args = ", ".join(arg for arg in module.arguments())
        
        content = "\n\n".join((
            f"[bold cyan]Arguments:[/bold cyan] {args}",
            f"[bold cyan]Description:[/bold cyan] "
            f"[bright_White]{module.description}[/bright_white]"
        ))

        self.console.print(
            Panel(
                content,
                title=f"✗ [bold cyan]{module.name}[/bold cyan]",
                title_align="left",
                border_style="bright_white",
                expand=False
            )
        )