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

    @staticmethod
    def execute(func):
        """ Decorator to execute commands with argument parsing. """
        def wrapper(*args):
            sig = inspect.signature(func)
            params = list(sig.parameters.values())

            if len(args) != len(params):
                raise ValueError(f"Command Expected {len(params)} arguments, got {len(args)}.")

            return func(*args)
        return wrapper