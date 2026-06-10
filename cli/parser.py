from cli.format import Format, Colors


class Parser:
    def __init__(self):
        self.fmt = Format()

    def user_input(self, action: str) -> tuple | None:
        cmd = action.strip()
        if not cmd:
            return None

        parts = cmd.split()
        name = parts[0].lower()
        args = parts[1:]

        return name, args
    
    def module_result(self, result: dict) -> None:
        if not result:
            return
        
        if "error" in result:
            self.fmt.error(str(result["error"]))
            return
        
        result = result["result"]
        
        if isinstance(result, list):
            for r in result:
                self.fmt.success(r)

        elif isinstance(result, dict):
            largest_len = max(len(name) for name in result)

            for name, value in result.items():
                self.fmt.success(
                name + " " * ((largest_len - len(name)) + 1) +
                f"{Colors.CYAN}->{Colors.RESET} {value}"
            )

        elif isinstance(result, str):
            self.fmt.success(result)