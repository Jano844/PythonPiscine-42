



class calculator:

	@staticmethod
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		if len(V1) != len(V2):
			return
		val = sum([a * b for a, b in zip(V1, V2)])
		print(f"Dot product is: {val}")

	@staticmethod
	def add_vec(V1: list[float], V2: list[float]) -> None:
		if len(V1) != len(V2):
			return
		val = [a + b for a, b in zip(V1, V2)]
		print(f"Add Vector is: {val}")

	@staticmethod
	def sous_vec(V1: list[float], V2: list[float]) -> None:
		if len(V1) != len(V2):
			return
		val = [a - b for a, b in zip(V1, V2)]
		print(f"Sous Vector is: {val}")