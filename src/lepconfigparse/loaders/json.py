import json

from .types import Config
from .abstract import ConfigLoader


class JsonConfigLoader(ConfigLoader):
    def load(self, path: str) -> Config:
        with open(path, "r") as file:
            config: Config = json.load(file)
        return config

    def save(self, path: str, config: Config):
        with open(path, "w") as file:
            json.dump(config, file)
