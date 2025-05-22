


def square(x: int | float) -> int | float:
	return x * x


def pow(x: int | float) -> int | float:
	return x ** x

def outer(x: int | float, function) -> object:
	def inner() -> float:
		nonlocal x
		x = function(x)
		return x
	return inner

def main():
	num : int | float = 3
	print(square(num))
	print(pow(num))

	num = 0.5
	print(square(num))
	print(pow(num) * 2)

if __name__ == "__main__":
	main()