from typing import Self

from .argparsing import get_config_path, get_args, askfor_config_path
from .nesting import Config, gen_setdict, nest_dict, gen_getdict, gen_constants


class ConfigManager:
    """
    Class responsible for storing all variables and methods
    relevant to setting, saving and loading configuration files.
    """

    path_internal: str
    path_config: str | None
    path_constants: str | None

    def __init__(
        self: Self,
        path_internal: str,
        path_config: str | None = None,
        path_constants: str | None = None,
    ) -> None:
        self.path_internal = path_internal
        self.path_config = path_config
        self.path_constants = path_constants

    def load_config_from(self: Self, config_path: str) -> Config:
        pass

    def save_config_at(self: Self, internal_path: str, config: Config):
        pass

    def set_internal_config(self: Self):
        if self.path_config is None:
            args, rest = get_config_path()
        else:
            args, rest = askfor_config_path(self.path_config)

        config_path: str = args.config_path

        config = self.load_config_from(config_path)

        args = get_args(config, rest)

        lines = gen_setdict(nest_dict(config))
        for line in lines:
            exec(line)

        self.save_config_at(self.path_internal, config)

    def load_internal_config(self: Self):
        config = self.load_config_from(self.path_internal)

        lines = gen_getdict(nest_dict(config))
        for line in lines:
            exec(line, globals())

    def save_internal_constants(self: Self):
        if self.path_constants is None:
            raise ValueError(f"{self.__name__} has no path_constants variable set.")

        config = self.load_config_from(self.path_internal)

        lines = gen_constants(nest_dict(config))
        with open(self.path_constants, "w") as file:
            file.writelines(lines)
