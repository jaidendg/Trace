from core.base import Command
from core.registry import Registry
from cli.format import Format


class ModulesCommand(Command):
    name = "modules"
    description = "List all available modules."
    aliases = ["mods"]

    def __init__(self):
        self.registry = Registry()
        self.fmt = Format()

    @Command.execute
    def run(self):
        modules = self.registry.list_modules()

        if not modules:
            self.fmt.warn("No modules loaded.")
            return
        
        max_len = max(len(module["name"]) for module in  modules)
        desc_len = max(len(module["description"]) for module in modules)

        self.fmt.info(f"{'Name':{max_len}}   Description")
        self.fmt.info(f"{'-':-<{max_len}}   {'-' * desc_len}")

        for module in modules:
            name = module["name"]
            desc = module["description"]
            self.fmt.info(f"{name:{max_len}}   {desc}")

        print()