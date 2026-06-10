from cli.format import Format
from cli.parser import Parser
from core.registry import Registry
from core.executor import Executor


class Shell:

    def __init__(self):
        self.fmt = Format()
        self.parser = Parser()
        self.registry = Registry()
        self.executor = Executor()
        self.running = True

        self.registry.load_modules()

    def start(self) -> None:
        self.fmt.clear()

        while self.running:
            try:
                action = self.fmt.input()
                self.handle(action)
            except KeyboardInterrupt:
                self.fmt.error("Exiting...\n")
                self.running = False

    def handle(self, action: str) -> None:
        cmd = self.parser.user_input(action)

        if not cmd:
            return

        name, args = cmd
        if name == "run" and len(args) < 2:
            self.fmt.error("Missing arguments.")
            return

        match (name):
            case "run":
                module = self.registry.get_module(args[0])

                if not module:
                    self.fmt.error("Invalid module.")
                    return

                result = self.executor.run(module, *args[1:])
                self.parser.module_result(result)

            case "modules":
                for module in self.registry.list_modules():
                    self.fmt.info(module["name"] + " - " + module["description"])

            case "clear" | "cls":
                self.fmt.clear()

            case "exit":
                self.running = False

            case "help":
                self.fmt.show_help()

            case _:
                self.fmt.error("Invalid command.")