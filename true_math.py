from math import inf


def divide(first, second, res=None):
    if second == 0:
        res = inf
        return res
    res = first/second
    return res