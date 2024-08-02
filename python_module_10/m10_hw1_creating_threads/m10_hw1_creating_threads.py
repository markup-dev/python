from threading import Thread
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
	for i in range(word_count):
		with open(file_name, 'a', encoding='utf-8') as f:
			f.write(f'Какое-то слово № {i + 1}\n')
			sleep(0.1)
	print(f'Завершилась запись в файл {file_name}')


time_start_1 = datetime.now()


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end_1 = datetime.now()

print(f'Работа потоков {time_end_1 - time_start_1}')

time_start_2 = datetime.now()

the_first = Thread(target=write_words, args=(10, 'example5.txt'))
the_second = Thread(target=write_words, args=(30, 'example6.txt'))
the_third = Thread(target=write_words, args=(200, 'example7.txt'))
the_forth = Thread(target=write_words, args=(100, 'example8.txt'))

the_first.start()
the_second.start()
the_third.start()
the_forth.start()

the_first.join()
the_second.join()
the_third.join()
the_forth.join()

time_end_2 = datetime.now()

print(f'Работа потоков {time_end_2 - time_start_2}')
