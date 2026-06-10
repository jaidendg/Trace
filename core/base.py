from abc import ABC, abstractmethod


class BaseModule(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def run(self, *args, **kwargs) -> dict:
        pass