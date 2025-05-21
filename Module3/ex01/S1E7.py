from S1E9 import Character


class Baratheon(Character):
	"""This class represents a member of House Baratheon."""

	def __init__(self, first_name: str, is_alive: bool = True):
		"""Init Baratheon Charactor"""
		super().__init__(first_name, is_alive)
		self.family_name = "Baratheon"
		self.eyes = "brown"
		self.hairs = "dark"
	
	def __str__(self):
		if not self.is_alive:
			return f"{self.first_name} is from the House of {self.family_name} and is dead"
		return f"{self.first_name} is from the House of {self.family_name} and is alive"


	def __repr__(self):
		return (
			f"<{self.family_name}(name='{self.first_name}', alive={self.is_alive}, "
			f"family_name={self.family_name}, eyes={self.eyes}, hairs={self.hairs})>"
		)

	
	def die(self):
		"""The character as dead."""
		self.is_alive = False
		print(f"{self.first_name} has died")
	
	

class Lannister(Character):
	"""This class represents a member of House Lannister."""

	def __init__(self, first_name: str, is_alive: bool = True):
		"""Init Lannister Character"""
		super().__init__(first_name, is_alive)
		self.family_name = "Lannister"
		self.eyes = "blue"
		self.hairs = "light"

	def __str__(self):
		if not self.is_alive:
			return f"{self.first_name} is from the House of {self.family_name} and is dead"
		return f"{self.first_name} is from the House of {self.family_name} and is alive"

	def __repr__(self):
		return (
			f"<{self.family_name}(name='{self.first_name}', alive={self.is_alive}, "
			f"family_name={self.family_name}, eyes={self.eyes}, hairs={self.hairs})>"
		)
	
	def die(self):
		"""The character as dead."""
		self.is_alive = False
		print(f"{self.first_name} has died")

	@classmethod
	def create_lannister(cls, first_name: str, is_alive: bool = True):
		return cls(first_name, is_alive)