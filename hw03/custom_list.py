"""
Module for CustomList class
"""


class CustomList(list):
    """
    List with addition, subtraction and sum for comparison
    """
    def __add__(self, other):
        result = CustomList([0] * max(len(self), len(other)))
        for i in range(min(len(self), len(other))):
            result[i] = self[i] + other[i]
        if len(self) < len(other):
            for i in range(len(self), len(other)):
                result[i] = other[i]
        else:
            for i in range(len(other), len(self)):
                result[i] = self[i]
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        result = CustomList([0] * len(self))
        for i, val in enumerate(self):
            result[i] = -val
        return result

    def __sub__(self, other):
        return self.__add__(-CustomList(other))

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __str__(self):
        return super().__str__() + ' sum ' + str(sum(self))
