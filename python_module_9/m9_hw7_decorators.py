def is_prime(func):
	def wrapper(num_1, num_2, num_3):
		res = func(num_1, num_2, num_3)
		flag = True
		for i in range(res):
			for j in range(2, res):
				if res % j != 0:
					continue
				else:
					flag = False
		if flag:
			return f'Простое\n{res}'
		else:
			return f'Составное\n{res}'

	return wrapper


@is_prime
def sum_three(num_1, num_2, num_3):
	return num_1 + num_2 + num_3


result = sum_three(2, 3, 6)
print(result)
