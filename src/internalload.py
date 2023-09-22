import json
import pathlib
from typing import Any

Config = dict[str, Any]
FILE_RECENT_CONFIG = "config-internal/config-recent.json"
FILE_CONSTANTS = "constants.py"


def generate_internal_config_path(
    file_config: str = FILE_RECENT_CONFIG,
) -> str:
    return (pathlib.Path(__file__).parent / file_config).__str__()


def generate_constants_path(file_constants: str = FILE_CONSTANTS) -> str:
    return (pathlib.Path(__file__).parent / file_constants).__str__()


def load_internal(
    config_path: str = generate_internal_config_path(),
) -> Config:
    with open(config_path, "r") as file:
        config = json.loads(file.read())
    print(f"Load from {config_path}")
    return config


def set_internal(
    config: Config,
    config_path: str = generate_internal_config_path(),
):
    with open(config_path, "w") as file:
        file.write(json.dumps(config))
        print(f"Wrote to {config_path}")
