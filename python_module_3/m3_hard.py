def calculate_structure_sum(data_struct):
	total_sum = 0
	if isinstance(data_struct, (int, float)):
		return data_struct
	elif isinstance(data_struct, str):
		return len(data_struct)
	elif isinstance(data_struct, (list, tuple, set)):
		for item in data_struct:
			total_sum += calculate_structure_sum(item)
	elif isinstance(data_struct, dict):
		for key, value in data_struct.items():
			total_sum += calculate_structure_sum(key)
			total_sum += calculate_structure_sum(value)
	elif isinstance(data_struct, tuple):
		for item in data_struct:
			total_sum += calculate_structure_sum(item)
	return total_sum


data_structure = [
	[1, 2, 3],
	{'a': 4, 'b': 5},
	(6, {'cube': 7, 'drum': 8}),
	"Hello",
	((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
