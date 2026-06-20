from cli.format import Format, Colors
from core.base import Result


class Parser:
    def __init__(self):
        self.fmt = Format()

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
            for r in result.data:
                self.fmt.success(str(r))

        elif isinstance(result.data, dict):
            largest_len = max(len(name) for name in result.data.keys())

            for name, value in result.data.items():
                self.fmt.success(f"{name:{largest_len}} {Colors.CYAN}->{Colors.RESET} {value}")

        else:
            self.fmt.success(str(result.data))