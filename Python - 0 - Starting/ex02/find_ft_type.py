def all_thing_is_obj(object: any) -> int:
	try:
		mytype = type(object)
		if isinstance(object, str):
			print(f"{object} is in the kitchen : " + str(mytype))
		elif isinstance(object, int):
			print(f"Type not found")
		else:
			print(mytype.__name__.capitalize() + " : " + str(mytype))
	except AttributeError:
		print("Type not found")
	return 42