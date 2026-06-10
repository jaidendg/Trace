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

        self.fmt.clear()
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
                self.fmt.error(f"Exception error: {e}")

    def handle(self, action: str) -> None:
        cmd = self.parser.user_input(action)

        if not cmd:
            return

        action, args = cmd

        match action:
            case "run":
                if not args:
                    self.fmt.error("Usage: run <module> <args>")
                    return
                
                module_name = args[0]
                module_args = args[1:]
                if not module_args:
                    self.fmt.error("Missing module arguments.")
                    return

                module = self.registry.get_module(module_name)

                if not module:
                    self.fmt.error(f"Module '{module_name}' not found.")
                    return

                result = self.executor.run(module, *module_args)
                self.parser.module_result(result)

            case "modules":
                for module in self.registry.list_modules():
                    self.fmt.info(module["name"] + " - " + module["description"])

                print()

            case "clear" | "cls":
                self.fmt.clear()

            case "exit" | "quit":
                self.running = False

            case "help":
                self.fmt.show_help()

            case _:
                self.fmt.error(f"Invalid command: '{action}'")