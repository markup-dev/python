first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(line_1) - len(line_2) for line_1, line_2 in zip(first, second) if len(line_1) != len(line_2))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))
