from core.base import Command
from core.registry import Registry
from cli.format import Format

from rich.console import Console
from rich.table import Table
from rich import box


class HelpCommand(Command):
    name = "help"
    description = "Show this help message."
    aliases = ["?"]

    def __init__(self):
        self.registry = Registry()
        self.fmt = Format()
        self.console = Console()

    @Command.execute
    def run(self):
        commands = self.registry.list_commands()
        if not commands:
            self.fmt.warn("No commands loaded.")
            return

        table = Table(
            title="Available Commands",
            title_style="bold cyan",
            box=box.ROUNDED
        )
        table.add_column("Command", header_style="cyan")
        table.add_column("Aliases", header_style="cyan")
        table.add_column("Description", header_style="cyan")

        for cmd in commands:
            aliases = ", ".join(cmd["aliases"] if cmd["aliases"] else "")
            table.add_row(cmd["name"], aliases, cmd["description"])

        self.console.print()
        self.console.print(table)
        self.console.print()