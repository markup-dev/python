class House:
	def __init__(self):
		self.number_of_floors = 0

	def set_new_number_of_floors(self, floors):
		self.number_of_floors = floors
		print(self.number_of_floors)


home = House()
home.set_new_number_of_floors(5)
