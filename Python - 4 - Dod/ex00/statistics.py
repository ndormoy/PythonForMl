def ft_mean(*args):
    """Calculate the mean of args"""
    mean = (sum(arg for arg in args)) / len(args)
    # print(f"mean : {mean}")
    return mean


def ft_median(*args):
    """Calculate the median of args"""
    n = len(args)
    index = n // 2
    # Sample with an odd number of observations
    if n % 2:
        return sorted(args)[index]
    # Sample with an even number of observations
    return sum(sorted(args)[index - 1:index + 1]) / 2


def ft_quartile(*args):
    """Calculate the quartile of args"""
    sorted_data = sorted(args)
    n = len(sorted_data)
    q1_index = int(n * 0.25)
    q3_index = int(n * 0.75)
    q1 = float(sorted_data[q1_index])
    q3 = float(sorted_data[q3_index])
    return [q1, q3]


def ft_variance(*args):
    """Calculate the variance"""
    n = len(args)
    if n < 2:
        return None
    mean = ft_mean(*args)
    # Find each score’s deviation from the mean and square
    score_deviation = [(arg - mean) ** 2 for arg in args]
    # Find the sum of squares
    sum_of_square = sum(score_deviation)
    # Find the variance
    variance = sum_of_square / n
    return variance


def ft_standart_deviation(*args):
    """Calculate standart deviation"""
    n = len(args)
    if n < 2:
        return None
    variance = ft_variance(*args)
    # Find the square root of the variance
    standard_deviation = variance ** 0.5
    return standard_deviation


def check_args(*args, **kwargs):
    if args:
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("args must be integers")
    if not kwargs:
        raise TypeError("Must have some kwargs")


def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        check_args(*args, **kwargs)
        for key, value in kwargs.items():
            if args:
                if value == "mean":
                    print(f"mean : {ft_mean(*args)}")
                elif value == "median":
                    print(f"median : {ft_median(*args)}")
                elif value == "quartile":
                    print(f"quartile : {ft_quartile(*args)}")
                elif value == "std":
                    print(f"std : {ft_standart_deviation(*args)}")
                elif value == "var":
                    print(f"var : {ft_variance(*args)}")
            else:
                print("ERROR")

    except TypeError as e:
        print(e)
