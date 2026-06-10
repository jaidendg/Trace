import importlib
import pkgutil
import modules

from core.base import BaseModule


class Registry:
    def __init__(self):
        self.modules = {}

    def register_module(self, module: BaseModule) -> None:
        self.modules[module.name] = module

    # thanks to whoever i stole this from
    def load_modules(self) -> None:
        for _, name, _ in pkgutil.iter_modules(modules.__path__):
            mod = importlib.import_module(f"modules.{name}")

            for attr in dir(mod):
                obj = getattr(mod, attr)

                if (
                    isinstance(obj, type)
                    and issubclass(obj, BaseModule)
                    and obj is not BaseModule
                ):
                    self.register_module(obj())

    def get_module(self, name: str) -> BaseModule | None:
        return self.modules.get(name)

    def list_modules(self) -> list[dict]:
        return [
            {
                "name": module.name,
                "description": module.description
            } for module in self.modules.values()
        ]