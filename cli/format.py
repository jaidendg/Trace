import os
from colorama import Fore, Style, init

init(autoreset=True)


class Colors:
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    RED = Fore.RED
    CYAN = Fore.LIGHTCYAN_EX
    RESET = Style.RESET_ALL

class Format:

    def ascii_art(self) -> str:
        return f"""{Colors.CYAN}
  _______                 
 |__   __|                             ))
    | |_ __ __ _  ___ ___            .-#-----.
    | | '__/ _` |/ __/ _ \\          /_________\\
    | | | | (_| | (_|  __/           |[] _ []|
    |_|_|  \__,_|\___\___|           |  |*|  |
{Colors.RESET}       OSINT Framework        Type 'help' for commands            
"""

    def clear(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        print(self.ascii_art())

    def input(self) -> str:
        user_input = input(f"trace~{Colors.CYAN}${Colors.RESET} ")
        return user_input

    def _print(self, prefix: str, message: str, **kwargs) -> None:
        print(f"{prefix} {message}", **kwargs)

    def info(self, message: str, **kwargs) -> None:
        self._print(f"[{Colors.CYAN}*{Colors.RESET}]", message, **kwargs)

    def success(self, message: str, **kwargs) -> None:
        self._print(f"[{Colors.GREEN}+{Colors.RESET}]", message, **kwargs)

    def warn(self, message: str, **kwargs) -> None:
        self._print(f"[{Colors.YELLOW}!{Colors.RESET}]", message, **kwargs)

    def error(self, message: str, **kwargs) -> None:
        self._print(f"[{Colors.RED}-{Colors.RESET}]", message, **kwargs)

    def show_help(self) -> None:
        self.info("Name                         Description")
        self.info("-------------------          ---------------------")
        self.info("run / use <module> <args>    Run a module.")
        self.info("modules                      List all modules.")
        self.info("info <module>                Gets info about a module.")
        self.info("clear / cls                  Clear screen.")
        self.info("exit / quit                  Exit framework.")
        self.info("help                         Show this help menu.\n")

    def display_modules(self, modules: list) -> None:
        if not modules:
            self.warn("No modules loaded.")
            return
        
        max_len = max(len(module["name"]) for module in  modules)
        self.info("Name" + " " * (max_len - 4) + "   Description")
        self.info("-" * max_len + "   " + "-" * 45)

        for module in modules:
            name = module["name"]
            desc = module["description"]
        
            self.info(name + " " * (max_len - len(name)) + "   " + desc)
        print()