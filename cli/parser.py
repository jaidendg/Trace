from cli.format import Format, Colors
from dataclasses import dataclass

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
    
    def parse_result(self, result: dict) -> None:
        if not result:
            return
        
        if "error" in result:
            self.fmt.error(str(result["error"]))
            return
        
        result = result["result"]
        if not result:
            return
        
        if isinstance(result, list):
            for r in result:
                self.fmt.success(str(r))

        elif isinstance(result, dict):
            largest_len = max(len(name) for name in result)

            for name, value in result.items():
                self.fmt.success(f"{name:{largest_len}} {Colors.CYAN}->{Colors.RESET} {value}")

        else:
            self.fmt.success(str(result))