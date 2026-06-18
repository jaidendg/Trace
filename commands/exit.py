import sys
from core.base import Command


class ExitCommand(Command):
    name = "exit"
    description = "Exit the application."
    aliases = ["quit"]

    @Command.execute
    def run(self):
        sys.exit(0)