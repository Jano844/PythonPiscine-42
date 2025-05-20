def NULL_not_found(object: any) -> int:
	if object is None:
		print(f"Nothing: None {type(object)}")
		return 0
	elif isinstance(object, float) and str(object) == 'nan':
		print(f"Cheese: nan {type(object)}")
		return 0
	elif object == 0 and type(object) == int:
		print(f"Zero: 0 {type(object)}")
		return 0
	elif object == '' and isinstance(object, str):
		print(f"Empty: {type(object)}")
		return 0
	elif object is False:
		print(f"Fake: False {type(object)}")
		return 0
	else:
		print(f"Type not found")
		return 1