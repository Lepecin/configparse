from .internalload import load_internal
from .setconfig.todict import nest_dict, gen_getdict

from .constants import *

config = load_internal()
lines = gen_getdict(nest_dict(config))
for line in lines:
    exec(line)
