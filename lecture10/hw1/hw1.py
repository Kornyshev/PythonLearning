"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    def __new__(metacls, cls, bases, classdict):
        if f'_{cls}__keys' in classdict and isinstance(classdict[f'_{cls}__keys'], tuple):
            keys = classdict[f'_{cls}__keys']
            simple_enum_cls = super().__new__(metacls, cls, bases, classdict)
            simple_enum_cls._member_names_ = set(keys)
            for attr in simple_enum_cls._member_names_:
               setattr(simple_enum_cls, attr, attr)
            return simple_enum_cls
        else:
            return super().__new__(metacls, cls, bases, classdict)


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


if __name__ == '__main__':
    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"
