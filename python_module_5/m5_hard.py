import time


class UrTube:
	users = []
	videos = []
	current_user = None

	def log_in(self, login, password):
		for user in self.users:
			if user.nickname == login and user.password == hash(password):
				self.current_user = user
				break

	def register(self, nickname, password, age):
		for user in self.users:
			if user.nickname == nickname:
				print(f"Пользователь {nickname} уже существует")
				return
		self.current_user = User(nickname, password, age)
		self.users.append(self.current_user)

	def log_out(self):
		self.current_user = None

	def add(self, *videos):
		for video in videos:
			if video != self.videos:
				self.videos.append(video)

	def get_videos(self, query):
		query = query.lower()
		return [video.title for video in self.videos if query in video.title.lower()]

	def watch_video(self, video_title):
		if not self.current_user:
			print("Войдите в аккаунт, чтобы смотреть видео")
			return
		for video in self.videos:
			if video.title == video_title:
				if video.adult_mode and self.current_user.age < 18:
					print("Вам нет 18 лет, пожалуйста покиньте страницу")
					return
				for i in range(1, video.duration + 1):
					time.sleep(1)
					print(i, end=' ')
				print("Конец видео")


class Video:
	def __init__(self, title, duration, time_now=0, adult_mode=False):
		self.title = title
		self.duration = duration
		self.time_now = time_now
		self.adult_mode = adult_mode


class User:
	def __init__(self, nickname, password, age):
		self.nickname = nickname
		self.password = hash(str(password))
		self.age = age

	def __str__(self):
		return self.nickname


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
