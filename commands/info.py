from core.base import Command
from core.registry import Registry
from cli.format import Format


class InfoCommand(Command):
    name = "info"
    description = "Show information about a module."
    aliases = []

    def __init__(self):
        self.registry = Registry()
        self.fmt = Format()

    @Command.execute
    def run(self, module_name: str):
        module = self.registry.get_module(module_name)

        if not module:
            self.fmt.error(f"Module '{module_name}' not found.")
            return

        module_args = module.arguments()
        max_len = max(len(args) for args in module_args) + 6

        self.fmt.info(f"{'Args':{max_len}}Description")
        self.fmt.info(f"{'----':{max_len}}-----------")

        first_arg = module_args[0]
        self.fmt.info(f"{first_arg:{max_len}}{module.description}")

        for arg in module_args[1:]:
            self.fmt.info(arg)
        
        print()