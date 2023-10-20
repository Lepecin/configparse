from abc import ABC, abstractmethod

from .types import Config


class __ConfigLoaderAbstract(ABC):
    """
    Abstract class for loading and saving config style
    objects into a Python environment.

    Has two methods, a getter and a setter for modifying
    the state of the machine file system.
    - load (getter)
    - save (setter)
    """

    @abstractmethod
    def load(self, path: str) -> Config:
        pass

    @abstractmethod
    def save(self, path: str, config: Config):
        pass


class ConfigLoader(__ConfigLoaderAbstract):
    pass
