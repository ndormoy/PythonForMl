def square(x: int | float) -> int | float:
    """Square function"""
    assert isinstance(x, int) or isinstance(x, float), "must be int or float"
    try:
        return x ** 2
    except AssertionError as e:
        print(e)



def pow(x: int | float) -> int | float:
    """pow function"""
    assert isinstance(x, int) or isinstance(x, float), "must be int or float"
    try:
        return x ** x
    except AssertionError as e:
        print(e)


def outer(x: int | float, function) -> object:
    count = 0
    def inner() -> float:   
        nonlocal x
        x = function(x)
        return x
    return inner