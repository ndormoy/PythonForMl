def ft_filter(function, iterable):
    """Ft Filter function"""
    for x in iterable:
        if function(x):
            yield x
