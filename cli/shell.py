from cli.format import Format
from cli.parser import Parser
from core.registry import Registry


class Shell:

    def __init__(self):
        self.fmt = Format()
        self.parser = Parser()
        self.registry = Registry()
        self.running = True

        self.fmt.clear()
        self.registry.load_commands()
        self.registry.load_modules()

    def start(self) -> None:
        while self.running:
            try:
                action = self.fmt.input()
                self.handle(action)
            except KeyboardInterrupt:
                self.fmt.error("Exiting...\n")
                self.running = False
            except Exception as e:
                self.fmt.error(f"Exception: {e}")

    def handle(self, action: str) -> None:
        parsed_input = self.parser.parse_input(action)
        if not parsed_input:
            return

        command, args = parsed_input
        command = self.registry.get_command(command)
        if not command:
            self.fmt.error(f"Invalid command: '{action}'")
            return
    
        command.run(*args)