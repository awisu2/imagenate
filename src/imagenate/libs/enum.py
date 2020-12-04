from enum import Enum


class CustomEnum(Enum):
    @classmethod
    def get_values(cls):
        values = []
        for e in list(cls):
            values.append(e.value)
        return values

    @classmethod
    def get(cls, v, default=None) -> Enum:
        values = cls.get_values()
        if v in values:
            return cls[v]
        return default

    @classmethod
    def is_exist(cls, v) -> bool:
        values = cls.get_values()
        return v in values
