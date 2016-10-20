import json

from .traversable import Traversable


def load(*args, **kwargs):
    j = json.load(*args, **kwargs)
    return Traversable(j)


def loads(*args, **kwargs):
    j = json.loads(*args, **kwargs)
    return Traversable(j)


def dump(obj, *args, **kwargs):
    if isinstance(obj, Traversable):
        obj = obj._obj
    return json.dump(obj, *args, **kwargs)


def dumps(obj, *args, **kwargs):
    if isinstance(obj, Traversable):
        obj = obj._obj
    return json.dumps(obj, *args, **kwargs)


def from_dict(jdict):
    return Traversable(jdict)


def new(kind=dict):
    return Traversable(kind())
