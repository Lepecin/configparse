from typing import Any, Self

Config = dict[str, Any]


class ConfigLoader:
    def load(self: Self, config_path: str) -> Config:
        pass

    def save(self: Self, config_path: str, config: Config):
        pass
