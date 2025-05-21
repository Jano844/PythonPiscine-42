from abc import ABC, abstractmethod


class Character(ABC):
	@abstractmethod
	def __init__(self, first_name: str, is_alive: bool = True):
		self.first_name = first_name
		self.is_alive = is_alive

	@abstractmethod
	def die(self):
		pass

class Stark(Character):
	"""This class represents a member of House Stark."""

	def __init__(self, first_name: str, is_alive: bool = True):
		"""Initialize a Stark character."""
		super().__init__(first_name, is_alive)
	
	def die(self):
		"""The character as dead."""
		self.is_alive = False
		print(f"{self.first_name} has died")