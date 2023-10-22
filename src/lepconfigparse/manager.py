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
    verbose: bool

    def __init__(
        self,
        path_internal: str,
        config_loader: ConfigLoader,
        *,
        verbose: bool = False,
    ) -> None:
        self.path_internal = path_internal
        self.config_loader = config_loader
        self.verbose = verbose

    def load_config_from(self, config_path: str) -> Config:
        try:
            print(f"Loading from {config_path}.") if self.verbose else None
            return self.config_loader.load(config_path)
        except FileNotFoundError:
            print(
                f"No file {config_path} found. Loading empty config."
            ) if self.verbose else None
            return {}

    def save_config_at(self, config_path: str, config: Config):
        print(f"Saving to {config_path}") if self.verbose else None
        self.config_loader.save(config_path, config)

    def save_internal_config(self, default_config_path: str | None = None):
        config_path, rest = get_config_path(default_config_path)
        config = self.load_config_from(config_path)
        args = get_args(config, rest)
        config = args_to_config(config, args)
        self.save_config_at(self.path_internal, config)

    def load_internal_config(self) -> Config:
        config = self.load_config_from(self.path_internal)

        return gen_getdict(nest_dict(config))

    def save_internal_constants(self, path_constants: str):
        config = self.load_config_from(self.path_internal)

        lines = gen_constants(nest_dict(config))
        with open(path_constants, "w") as file:
            file.writelines(lines)
