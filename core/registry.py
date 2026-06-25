import importlib
import pkgutil
import modules
import commands

from core.base import Module, Command


class Registry:
    def __init__(self):
        self.modules = {}
        self.commands = {}

    """ Modules registry. """    

    def register_module(self, module: Module) -> None:
        self.modules[module.name] = module

    def load_modules(self) -> None:
        self.modules.clear()

        for _, name, _ in pkgutil.iter_modules(modules.__path__):
            mod = importlib.import_module(f"modules.{name}")
            mod = importlib.reload(mod)

            for attr in dir(mod):
                obj = getattr(mod, attr)

                if (
                    isinstance(obj, type)
                    and issubclass(obj, Module)
                    and obj is not Module
                ):
                    self.register_module(obj())

    def get_module(self, name: str) -> Module | None:
        return self.modules.get(name)

    def list_modules(self) -> list[dict]:
        return [
            {
                "name": module.name,
                "description": module.description
            } for module in self.modules.values()
        ]

    """ Commands registry. """

    def register_command(self, command: Command) -> None:
        self.commands[command.name] = command

    def load_commands(self) -> None:
        self.commands.clear()

        for _, name, _ in pkgutil.iter_modules(commands.__path__):
            mod = importlib.import_module(f"commands.{name}")
            mod = importlib.reload(mod)

            for attr in dir(mod):
                obj = getattr(mod, attr)

                if (
                    isinstance(obj, type)
                    and issubclass(obj, Command)
                    and obj is not Command
                ):
                    self.register_command(obj())

    def get_command(self, name: str) -> Command | None:
        cmd = self.commands.get(name)
        if cmd:
            cmd.registry = self
            return cmd
        
        for cmd in self.commands.values():
            if cmd.aliases and name in cmd.aliases:
                cmd.registry = self
                return cmd

    def list_commands(self) -> list[dict]:
        return [
            {
                "name": command.name,
                "description": command.description,
                "aliases": command.aliases
            } for command in self.commands.values()
        ]