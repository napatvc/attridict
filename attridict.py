"""
    attridict.py:
        Alvin Shaita <alvinshaita@gmail.com>
"""

__author__ = "Alvin Shaita"
__email__ = "alvinshaita@gmail.com"
__version__ = "0.0.7"

import types
from mixins import MapMixin

__all__ = ["AttriDict"]


class _AttriDict(types.ModuleType):
    def __call__(self, *args, **kwargs):
        return AttriDict(*args, **kwargs)


class AttriDict(dict, MapMixin):
    """AttriDict"""

    def __init__(self, *args, **kwargs):
        if args and not isinstance(*args, dict):
            raise AttributeError(
                "non dict argument provided"
            )
        super().__init__(*args, **kwargs)

    def _attrify(self, obj):
        """
        Convert dict instance objects to attridict
        """
        if isinstance(obj, dict):
            obj = type(self)(obj)
        elif isinstance(obj, (list, set, tuple)):
            obj = type(obj)(self._attrify(i) for i in obj)

        return obj

    def _valid_key(self, key):
        """
        Check if the key provided is a valid key
        """
        if key in dir(self):
            return False

        return True

    def to_dict(self):
        """
        Return a dict equivalent of the attridict object
        """
        return dict(self)


if __name__ == "attridict":
    import sys

    sys.modules[__name__].__class__ = _AttriDict
