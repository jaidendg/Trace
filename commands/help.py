from core.base import Command
from core.registry import Registry
from cli.format import Format


class HelpCommand(Command):
    name = "help"
    description = "Show this help message."
    aliases = ["?"]

    def __init__(self):
        self.registry = Registry()
        self.fmt = Format()

    @Command.execute
    def run(self):
        commands = self.registry.list_commands()
        if not commands:
            self.fmt.warn("No commands loaded.")
            return
        
        max_len = max((len(cmd["name"]) for cmd in commands), default=6)
        alias_len = max((len(", ".join(cmd["aliases"])) for cmd in commands), default=7)
        desc_len = max((len(cmd["description"]) for cmd in commands), default=11)

        self.fmt.info(f"{'Command':{max_len}}   {'Aliases':{alias_len}}   Description")
        self.fmt.info(f"{'-':-<{max_len}}   {'-':-<{alias_len}}   {'-' * desc_len}")
    
        for cmd in commands:
            name = cmd["name"]
            aliases = ", ".join(cmd["aliases"]) if cmd["aliases"] else ""
            desc = cmd["description"]
            self.fmt.info(f"{name:{max_len}}   {aliases:{alias_len}}   {desc}")
    
        print()