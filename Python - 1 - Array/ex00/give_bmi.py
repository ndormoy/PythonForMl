import sys

sys.tracebacklimit = 0


def all_float_or_int(lst):
    """Check if list is full of floats or ints"""
    for element in lst:
        if not isinstance(element, (float, int)):
            return False
    return True


def calculate_bmi(height, weight):
    """
    Calculates BMI (Body Mass Index) given height and weight.

    Args:
        height (float): Height in meters.
        weight (float): Weight in kilograms.

    Returns:
        float: Calculated BMI value.
    """
    bmi = weight / (height ** 2)
    return bmi


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate bmi for a given height and weight"""
    assert sys.getsizeof(height) == sys.getsizeof(weight),\
        "height and weight must have the same size"
    assert all_float_or_int(height) and all_float_or_int(weight),\
        "height and weight must be int or float"
    try:
        bmi_list = []
        for i in range(len(height)):
            bmi_list.append(calculate_bmi(height[i], weight[i]))
    except AssertionError as e:
        print(e)
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Limits of bmi values"""
    assert all_float_or_int(bmi), "bmp must be a list with int or float"
    assert isinstance(limit, int), "limit must be an int"
    try:
        limits = []
        for x in bmi:
            limits.append(x > limit)
    except AssertionError as e:
        print(e)
    return limits
