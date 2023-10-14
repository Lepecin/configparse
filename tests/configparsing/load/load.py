import pathlib

from lepconfigparse import ConfigManager, JsonConfigLoader

path_internal = (pathlib.Path(__file__).parent.parent / "save/config.json").__str__()

manager = ConfigManager(
    path_internal,
    JsonConfigLoader(),
)

config = manager.load_internal_config()

globals().update(config)
__all__ = list(config.keys())
