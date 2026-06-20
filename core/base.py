import inspect
from abc import ABC, abstractmethod


class Module(ABC):
    """ Base class for modules. """

    @property
    @abstractmethod
    def name(self):
        """ Module name. """
        pass

    @property
    @abstractmethod
    def description(self):
        """ Brief description of the module. """
        pass

    @classmethod
    def arguments(cls):
        """ Extract arguments from the run method signature. """
        sig = inspect.signature(cls.run)
        return [param.name for param in sig.parameters.values() if param.name != "self"]

    @abstractmethod
    def run(self, *args, **kwargs) -> dict:
        """ Execute the module and return {'result': ...} or {'error': ...}. """
        pass


class Command(ABC):
    """ Base class for all commands. """

    @property
    @abstractmethod
    def name(self):
        """ Name of the command. """
        pass

    @property
    @abstractmethod
    def description(self):
        """ Brief description of the command. """
        pass

    @property
    def aliases(self):
        """ Returns a list of aliases for this command. """
        pass

    @abstractmethod
    def run(self, *args, **kwargs) -> None:
        """ Execute the command. """
        pass

    @staticmethod
    def execute(func):
        """ Decorator to execute commands with argument parsing. """
        def wrapper(*args):
            sig = inspect.signature(func)
            params = list(sig.parameters.values())

            required_params = [
                p for p in params 
                if p.default == inspect.Parameter.empty 
                and p.kind not in (
                    inspect.Parameter.VAR_POSITIONAL, 
                    inspect.Parameter.VAR_KEYWORD
                )
            ]

            if len(args) < len(required_params):
                raise ValueError(f"Command expected {len(required_params)} arguments, got {len(args)}.")

            return func(*args)
        return wrapper