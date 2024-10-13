import sqlite3


def initiate_db():
	connection = sqlite3.connect('Products.db')
	cursor = connection.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Products(
	id INT PRIMARY KEY,
	title TEXT NOT NULL,
	description TEXT,
	price INT NOT NULL
	);
	''')

	connection.commit()
	connection.close()


def get_all_products():
	connection = sqlite3.connect('Products.db')
	cursor = connection.cursor()

	products = cursor.execute('SELECT * FROM Products')
	products_list = products.fetchall()

	connection.commit()
	connection.close()
	return products_list


def add_products():
	connection = sqlite3.connect('Products.db')
	cursor = connection.cursor()

	for i in range(1, 5):
		cursor.execute(f'''
			INSERT INTO Products VALUES('{i}','Банан №{i}', 'Классный банан №{i}.', {i*100})
			''')

	connection.commit()
	connection.close()
