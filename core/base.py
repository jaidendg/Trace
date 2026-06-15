from abc import ABC, abstractmethod


class BaseModule(ABC):
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

    @property
    @abstractmethod
    def arguments(self):
        """ List of expected module arguments. """
        pass

    @abstractmethod
    def run(self, *args, **kwargs) -> dict:
        """ Execute the module and return {'result': ...} or {'error': ...}. """
        pass