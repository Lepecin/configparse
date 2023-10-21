import argparse

from .nesting import (
    Config,
    nest_dict,
    gen_setdict,
    key_to_identifier,
)

ARG_PREFIX = "--"
ARG_CONFIG_PATH = "config_path"


def get_config_path(
    path_default: str | None = None,
    arg_prefix: str = ARG_PREFIX,
    arg_config_path: str = ARG_CONFIG_PATH,
) -> tuple[str, list[str]]:
    parser = argparse.ArgumentParser()

    argument = arg_prefix + arg_config_path

    HELP_MESSAGE = "Path to config file."

    if not path_default is None:
        parser.add_argument(
            argument,
            required=False,
            default=path_default,
            type=str,
            help=HELP_MESSAGE,
        )
    else:
        parser.add_argument(
            argument,
            required=True,
            type=str,
            help=HELP_MESSAGE,
        )

    args, rest = parser.parse_known_args()
    path: str = args.__dict__[arg_config_path]

    return path, rest


def get_args(
    config: Config,
    rest: list[str],
    arg_prefix: str = ARG_PREFIX,
) -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    config_nest = nest_dict(config)
    config = {key_to_identifier(key): value for key, value in config_nest.items()}

    for arg_key, value in config.items():
        argument = arg_prefix + arg_key

        parser.add_argument(
            argument,
            required=False,
            type=value.__class__,
        )

    args = parser.parse_args(rest)

    config.update(
        {key: value for key, value in args.__dict__.items() if not value is None}
    )

    return argparse.Namespace(**config)


def args_to_config(config: Config, args: argparse.Namespace) -> Config:
    lines = gen_setdict(nest_dict(config))
    for line in lines:
        exec(line)
    return config
