def all_thing_is_obj(object: any) -> int:
	if (type(object) == list):
		print(f"List: {type(object)}")
	elif (type(object) == tuple):
		print(f"Tuple: {type(object)}")
	elif (type(object) == set):
		print(f"Set: {type(object)}")
	elif (type(object) == dict):
		print(f"Dict: {type(object)}")
	elif (type(object) == str):
		print(f"{object} is not in the kitchen : {type(object)}")
	else:
		print(f"Type not Found")

	return 42