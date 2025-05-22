




def callLimit(limit: int):
	def callLimiter(function):
		count = 0

		def limit_function(*args, **kwargs):
			nonlocal count
			if count < limit:
				count += 1
				return function(*args, **kwargs)
			else:
				print(f"Function '{function.__name__}' call limit reached ({limit} calls).")

		return limit_function

	return callLimiter



def my_decorator(func):
	def wrapper(*args, **kwargs):
		print("Wrapper begin")
		

		result = func(*args, **kwargs)
		
	
		print("Wrapper done")
		return result
	return wrapper
