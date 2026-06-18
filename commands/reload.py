from core.base import Command
from core.registry import Registry
from cli.format import Format


class ReloadCommand(Command):
    name = "reload"
    description = "Reloads all modules or commands."
    aliases = []

    def __init__(self):
        self.registry = Registry()
        self.fmt = Format()

    @Command.execute
    def run(self, target: str):
        if target == "commands":
            self.registry.load_commands()
            self.fmt.success("Commands reloaded successfully.")
            return

        elif target == "modules":
            self.registry.load_modules()
            self.fmt.success("Modules reloaded successfully.")
            return

        self.fmt.error("Invalid argument. Use 'commands' or 'modules'.")