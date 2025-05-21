

from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
	"""
	Diamond Trap:
	Inherrits from Both Parents all Functions and Attributes
	But if Both have the same Methode or Atrribute it inherrits From the Firts one
	in this example Baratheon
	"""
	def __init__(self, first_name: str, is_alive: bool = True):
		#calls The Baratheon __init__ 
		super().__init__(first_name, is_alive)
	
	# Property Getter/Setter für 'eyes'
	def get_eyes(self):
		return self.eyes
	
	def set_eyes(self, value):
		self.eyes = value
	
	# Property Getter/Setter für 'hairs'
	def get_hairs(self):
		return self.hairs
	
	def set_hairs(self, value):
		self.hairs = value