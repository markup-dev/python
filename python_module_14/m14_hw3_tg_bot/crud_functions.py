import sqlite3


def initiate_db():
	connection = sqlite3.connect('Products.db')
	cursor = connection.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Products(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	description TEXT,
	price INT NOT NULL
	);
	''')

	connection.commit()
	connection.close()

	connection = sqlite3.connect('Users.db')
	cursor = connection.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Users(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT NOT NULL,
	email TEXT NOT NULL,
	age INT NOT NULL,
	balance INT NOT NULL
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
			INSERT INTO Products VALUES({i}, 'Банан №{i}', 'Классный банан №{i}.', {i * 100})
			''')

	connection.commit()
	connection.close()


def is_included(username):
	connection = sqlite3.connect('Users.db')
	cursor = connection.cursor()

	user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,)).fetchone()
	connection.close()
	if user is None:
		return False
	else:
		return True


def add_user(username, email, age):
	connection = sqlite3.connect('Users.db')
	cursor = connection.cursor()

	if not is_included(username):
		cursor.execute(
			'''
			INSERT INTO Users (username, email, age, balance)
			VALUES (?, ?, ?, 1000)
			''', (username, email, age))
		connection.commit()
	connection.close()
