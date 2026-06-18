from core.base import Command
from cli.format import Format


class ClearCommand(Command):
    name = "clear"
    description = "Clear the console."
    aliases = ["cls"]

    def __init__(self):
        self.fmt = Format()

    @Command.execute
    def run(self):
        self.fmt.clear()