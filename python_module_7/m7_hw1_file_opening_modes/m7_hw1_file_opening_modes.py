class Product:
	def __init__(self, name, weight, category):
		self.name = name
		self.weight = weight
		self.category = category

	def __str__(self):
		return f'{self.name}, {self.weight}, {self.category}'


class Shop:
	def __init__(self, file_name='products.txt'):
		self.__file_name = file_name

	def get_products(self):
		file = open(self.__file_name, 'r')
		products = file.read()
		file.close()
		return products

	def add(self, *products):
		for product in products:
			if product.name not in self.get_products():
				file = open(self.__file_name, 'a')
				file.write(f'{product}\n')
				file.close()
			else:
				print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
