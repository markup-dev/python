def custom_write(file_name, *strings):
	lines = list(map(str, *strings))
	strings_positions = {}
	file = open(file_name, 'w', encoding='utf-8')
	for i in range(len(lines)):
		strings_positions[(i+1, file.tell())] = lines[i]
		file.write(f'{lines[i]}\n')
	file.close()
	return strings_positions


info = [
	'Text for tell.',
	'Используйте кодировку utf-8.',
	'Because there are 2 languages!',
	'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
	print(elem)
