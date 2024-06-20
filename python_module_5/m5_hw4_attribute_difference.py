class Building:
	total = 0

	def __init__(self):
		Building.total += 1

	def info(self):
		return self.total


spis = []
for i in range(40):
	spis.append(Building())
	print(spis[i].info())

