from core.base import Command
from core.executor import Executor
from core.registry import Registry
from cli.format import Format
from cli.parser import Parser


class RunCommand(Command):
    name = "run"
    description = "Run a module with the specified arguments."
    aliases = ["use", "execute"]

    def __init__(self):
        self.registry = Registry()
        self.fmt = Format()
        self.parser = Parser()
        self.executor = Executor()

    @Command.execute
    def run(self, module_name: str, *args):
        module = self.registry.get_module(module_name)
        if not module:
            self.fmt.error(f"Module '{module_name}' not found.")
            return

        if not args:
            self.fmt.warn(f"Usage: run {module.name} " + 
                          " ".join(f"<{arg}>" for arg in module.arguments()))
            return
        
        result = self.executor.run(module, *args)
        self.parser.parse_result(result)