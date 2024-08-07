from threading import Thread
from time import sleep


class Knight(Thread):
	def __init__(self, name, power):
		super().__init__()
		self.name = name
		self.power = power

	def run(self):
		days = 0
		print(f'{self.name}, на нас напали!')
		for i in range(100, 0, -self.power):
			days += 1
			print(f'{self.name} сражается {days} дней(дня)..., осталось, {i-self.power} воинов.')
			sleep(1.0)
		print(f'{self.name} одержал победу спустя {days} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')
