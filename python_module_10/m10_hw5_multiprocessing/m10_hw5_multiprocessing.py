from datetime import datetime
from multiprocessing.pool import Pool


def read_info(name):
	all_data = []
	with open(name, 'r') as f:
		while True:
			line = f.readline()
			if line:
				all_data.append(line.strip())
			else:
				break


if __name__ == '__main__':
	filenames = [f'./file {number}.txt' for number in range(1, 5)]

	# Линейный
	start = datetime.now()
	for filename in filenames:
		read_info(filename)
	end = datetime.now()
	print(end - start, 'линейный')

	# Многопроцессный
	start = datetime.now()
	with Pool() as pool:
		pool.map(read_info, filenames)
	end = datetime.now()
	print(end - start, 'многопроцессный')


