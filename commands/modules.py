from core.base import Command
from core.registry import Registry
from cli.format import Format

from rich.console import Console
from rich.table import Table
from rich import box


class ModulesCommand(Command):
    name = "modules"
    description = "List all available modules."
    aliases = ["mods"]

    def __init__(self):
        self.registry = Registry()
        self.fmt = Format()
        self.console = Console()

    @Command.execute
    def run(self):
        modules = self.registry.list_modules()

        if not modules:
            self.fmt.warn("No modules loaded.")
            return

        table = Table(
            title="Available Modules", 
            title_style="bold cyan",
            box=box.ROUNDED
        )
        table.add_column("Name", header_style="cyan")
        table.add_column("Description", header_style="cyan")

        for module in modules:
            name = module["name"]
            description = module["description"]
            table.add_row(name, description)
        
        self.console.print()
        self.console.print(table)
        self.console.print()