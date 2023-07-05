def NULL_not_found(object: any) -> int:
	mytype = type(object)
	if object is None:
		print("Nothing : None " + str(mytype))
	elif object is False:
		print("Fake : False " + str(mytype))
	elif object != object:
		print("Cheese : NaN " + str(mytype))
	elif object == "":
		print("Empty: " + str(mytype))
	elif object == 0:
		print("Zero : 0 " + str(mytype))
	else:
		print("Type not found")
	return 1