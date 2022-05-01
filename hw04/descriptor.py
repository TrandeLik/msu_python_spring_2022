"""
Descriptors for Integer, Unsigned and String
"""


class Integer:
    """
    Integer descriptor
    """
    def __init__(self):
        self.value = 0

    def __get__(self, obj, objtype):
        return self.value

    def __set__(self, obj, val):
        if isinstance(val, int):
            self.value = val
        else:
            raise ValueError


class PositiveInteger:
    """
    Unsigned descriptor
    """
    def __init__(self):
        self.value = 0

    def __get__(self, obj, objtype):
        return self.value

    def __set__(self, obj, val):
        if isinstance(val, int) and val >= 0:
            self.value = val
        else:
            raise ValueError


class String:
    """
    String descriptor
    """
    def __init__(self):
        self.value = ""

    def __get__(self, obj, objtype):
        return self.value

    def __set__(self, obj, val):
        if isinstance(val, str):
            self.value = val
        else:
            raise ValueError
