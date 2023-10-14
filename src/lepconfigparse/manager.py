from typing import Self

from .loaders import ConfigLoader
from .nesting import Config, nest_dict, gen_getdict, gen_constants
from .argparsing import get_config_path, get_args, args_to_config


class ConfigManager:
    """
    Class responsible for storing all variables and methods
    relevant to setting, saving and loading configuration files.
    """

    path_internal: str
    config_loader: ConfigLoader

    def __init__(self: Self, path_internal: str, config_loader: ConfigLoader) -> None:
        self.path_internal = path_internal
        self.config_loader = config_loader

    def load_config_from(self: Self, config_path: str) -> Config:
        return self.config_loader.load(config_path)

    def save_config_at(self: Self, config_path: str, config: Config):
        self.config_loader.save(config_path, config)

    def save_internal_config(self: Self, default_config_path: str | None = None):
        config_path, rest = get_config_path(default_config_path)
        config = self.load_config_from(config_path)
        args = get_args(config, rest)
        config = args_to_config(config, args)
        self.save_config_at(self.path_internal, config)

    def load_internal_config(self: Self) -> Config:
        config = self.load_config_from(self.path_internal)

        return gen_getdict(nest_dict(config))

    def save_internal_constants(self: Self, path_constants: str):
        config = self.load_config_from(self.path_internal)

        lines = gen_constants(nest_dict(config))
        with open(path_constants, "w") as file:
            file.writelines(lines)
