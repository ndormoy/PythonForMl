def ft_filter(function, iterable):
	for x in iterable:
		if function(x):
			yield x
