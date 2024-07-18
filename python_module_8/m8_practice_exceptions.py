def calc(line):
	operand_1, operation, operand_2 = line.split(' ')
	operand_1 = int(operand_1)
	operand_2 = int(operand_2)
	if operation == '+':
		print(f'Результат: {operand_1 + operand_2}')
	elif operation == '-':
		print(f'Результат: {operand_1 - operand_2}')
	elif operation == '*':
		print(f'Результат: {operand_1 * operand_2}')
	elif operation == '/':
		print(f'Результат: {operand_1 / operand_2}')
	elif operation == '//':
		print(f'Результат: {operand_1 // operand_2}')
	elif operation == '%':
		print(f'Результат: {operand_1 % operand_2}')


count = 0

with open('module8_dop/calc.txt', 'r') as file:
	for line in file:
		count += 1
		try:
			calc(line)
		except ValueError as exc:
			if 'unpack' in exc.args[0]:
				print(f'Ошибка в линии {count}, не хватает данных для ответа.')
			else:
				print(f'Ошибка в линии {count}, нельзя перевести в число.')
