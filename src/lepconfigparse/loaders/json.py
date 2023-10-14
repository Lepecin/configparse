import json
from typing import Self

from .types import Config
from .abstract import ConfigLoader


class JsonConfigLoader(ConfigLoader):
    def load(self: Self, path: str) -> Config:
        with open(path, "r") as file:
            config: Config = json.load(file)
        return config

    def save(self: Self, path: str, config: Config):
        with open(path, "w") as file:
            json.dump(config, file)
