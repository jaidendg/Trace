from core.base import Command
from core.registry import Registry
from cli.format import Format


class ReloadCommand(Command):
    name = "reload"
    description = "Reloads all modules or commands."

    def __init__(self):
        self.registry = Registry()
        self.fmt = Format()

    @Command.execute
    def run(self, target: str):
        if target == "commands":
            self.registry.load_commands()
            self.fmt.success("Commands reloaded successfully.")

        elif target == "modules":
            self.registry.load_modules()
            self.fmt.success("Modules reloaded successfully.")
        
        else:
            self.fmt.error("Invalid argument. Use 'commands' or 'modules'.")