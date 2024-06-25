class Database:
	def __init__(self):
		self.data = {}

	def add_user(self, username, pass_word):
		self.data[username] = pass_word


class User:
	"""
	Класс пользователя, содержащий атрибуты: логин, пароль
	"""

	def __init__(self, username, pass_word, password_confirm):
		self.username = username
		if pass_word == password_confirm:
			self.password = pass_word


if __name__ == '__main__':
	database = Database()
	while True:
		choice = int(input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n"))
		if choice == 1:
			login = input("Введите логин: ")
			password = input("Введите пароль: ")
			if login in database.data:
				if password == database.data[login]:
					print(f'Вход выполнен, {login}')
					break
				else:
					print("Неверный пароль.")
			else:
				print("Пользователь не найден.")
		if choice == 2:
			user = User(input("Введите логин: "), passw := input("Введите пароль: "),
									check_password := input("Повторите пароль: "))
			if passw != check_password:
				print("Пароли не совпадают, попробуйте еще раз.")
				continue
			database.add_user(user.username, user.password)
# print(database.data)

# print(User.__doc__)
