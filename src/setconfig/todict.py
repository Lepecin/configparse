from typing import Any

from ..internalload import Config

NAME_CONFIG = "config"
NAME_NAMESPACE = "args"

NestKey = tuple[str, ...]
NestConfig = dict[NestKey, Any]


def nest_dict(
    config: Config,
    keys: NestKey = (),
) -> NestConfig:
    new_dict = {}
    for key, value in config.items():
        assert isinstance(key, str), f"keys must be strings, get {key}"

        if not isinstance(value, dict):
            new_dict.update({keys + (key,): value})
        else:
            new_dict.update(nest_dict(value, keys + (key,)))
    return new_dict


def key_to_identifier(key: NestKey) -> str:
    identifier = "_".join(key)
    assert identifier.isidentifier(), f"'{identifier}' is not an identifier"
    return identifier


def key_to_constant(key: NestKey) -> str:
    return key_to_identifier(key).upper()


def key_to_dictindex(key: NestKey) -> str:
    return "".join([f"[{name.__repr__()}]" for name in key])


def gen_getdict(
    nest_dict: NestConfig,
    name_config: str = NAME_CONFIG,
) -> list[str]:
    lines: list[str] = []
    for key in nest_dict:
        name_constant = key_to_constant(key)
        name_dict = name_config + key_to_dictindex(key)
        lines.append(f"{name_constant} = {name_dict}")

    return lines


def gen_setdict(
    nest_dict: NestConfig,
    name_config: str = NAME_CONFIG,
    name_namespace: str = NAME_NAMESPACE,
) -> list[str]:
    lines: list[str] = []
    for key in nest_dict:
        name_identifier = name_namespace + "." + key_to_identifier(key)
        name_dict = name_config + key_to_dictindex(key)
        lines.append(f"{name_dict} = {name_identifier}")

    return lines


def gen_constants(nest_dict: NestConfig) -> list[str]:
    lines: list[str] = []
    for key, value in nest_dict.items():
        name_constant = key_to_constant(key)
        name_data = value.__class__.__name__
        lines.append(f"{name_constant}: {name_data}" + "\n")

    return lines
