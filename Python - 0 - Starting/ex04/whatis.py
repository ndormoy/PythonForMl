import sys

if (len(sys.argv) != 1):
	try:
		assert(not len(sys.argv) > 2), "AssertionError: more than one argument is provided"
	except AssertionError as e:
		print(e)
		exit(1)
	
	try:
		arg = sys.argv[1]
		assert arg.isdigit(), "AssertionError: argument is not an integer"
		arg = int(arg)
		if (arg % 2 == 0):
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except AssertionError as e:
		print(e)