

class calculator:
	"""
	This is small calculator
	it can do addition, multiplication, subtraction, division
	on Vectors
	"""
	def __init__(self, list: list[float | int]):
		self.list = list

	def __add__(self, value: int | float) -> None:
		ret = [i + value for i in self.list]
		self.list = ret
		print(ret)

	def __mul__(self, value: int | float) -> None:
		ret = [i * value for i in self.list]
		self.list = ret
		print(ret)
	
	def __sub__(self, value: int | float) -> None:
		ret = [i - value for i in self.list]
		self.list = ret
		print(ret)
	
	def __truediv__(self, value: int | float) -> None:
		if value == 0:
			print("Cant Divide by 0")
			return
		ret = [i // value for i in self.list]
		self.list = ret
		print(ret)
	