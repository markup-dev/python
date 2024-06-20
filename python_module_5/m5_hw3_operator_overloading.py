class Building:
	def __init__(self, number_of_floors, building_type):
		self.number_of_floors = number_of_floors
		self.building_type = building_type

	def __eq__(self, other):
		return self.number_of_floors == other.number_of_floors and self.building_type == other.building_type


b1 = Building(3, "Кирпичный")
b2 = Building(1, "Дом")
b3 = Building(3, "Кирпичный")

print(b1 == b2)
print(b1 == b3)
