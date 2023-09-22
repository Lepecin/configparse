import json

from .todict import nest_dict, gen_setdict, gen_constants
from .configload import get_config_path, get_args
from ..internalload import Config, set_internal, generate_constants_path

args, rest = get_config_path()

config_path: str = args.config_path

with open(config_path, "r") as file:
    config: Config = json.loads(file.read())

args = get_args(config, rest)

lines = gen_setdict(nest_dict(config))
for line in lines:
    exec(line)

set_internal(config)

constants_path = generate_constants_path()

lines = gen_constants(nest_dict(config))
with open(constants_path, "w") as file:
    file.writelines(lines)
