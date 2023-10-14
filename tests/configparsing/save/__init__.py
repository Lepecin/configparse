import pathlib

from lepconfigparse import ConfigManager, JsonConfigLoader

path_internal = (pathlib.Path(__file__).parent / "config.json").__str__()
path_constants = (pathlib.Path(__file__).parent.parent / "load/constants.py").__str__()

manager = ConfigManager(
    path_internal,
    JsonConfigLoader(),
)

manager.save_internal_config(path_internal)
manager.save_internal_constants(path_constants)
