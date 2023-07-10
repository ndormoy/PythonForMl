import sys
import numpy as np

sys.tracebacklimit = 0


def slice_me(family: list, start: int, end: int) -> list:
    """Slice the given family"""
    assert isinstance(family, list), "First argument must be a list"
    assert isinstance(start, int) and isinstance(end, int),\
        "Second and third arguments must be a int"
    try:
        sliced = np.array(family)
        print("My shape is ", np.array(family).shape)
        sliced = family[start:end]
        print("My new shape is ", np.array(sliced).shape)
    except AssertionError as e:
        print(e)
    return sliced
