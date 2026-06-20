from cli.format import Format, Colors
from core.base import Result

from rich.console import Console
from rich.tree import Tree


class Parser:
    def __init__(self):
        self.fmt = Format()
        self.console = Console()

    def parse_input(self, action: str) -> tuple[str, list[str]] | None:
        if not action or not action.strip():
            return None

        parts = action.strip().split()
        if not parts:
            return None

        command = parts[0].lower()
        args = parts[1:]

        return command, args
    
    def parse_result(self, result: Result) -> None:
        if not result:
            return
        
        if result.error:
            self.fmt.error(str(result.error))
            return
        
        if not result.data:
            return
        
        if isinstance(result.data, list):
            tree = Tree("[bold cyan]Results[/bold cyan]", guide_style="bold cyan")
            for r in result.data:
                tree.add(f"[bright_white]{r}[/bright_white]")
            
            self.console.print(tree)

        elif isinstance(result.data, dict):
            largest_len = max(len(name) for name in result.data.keys())

            for name, value in result.data.items():
                self.fmt.success(f"{name:{largest_len}} {Colors.CYAN}->{Colors.RESET} {value}")

        else:
            self.fmt.success(str(result.data))