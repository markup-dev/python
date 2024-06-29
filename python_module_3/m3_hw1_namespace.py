calls = 0


def count_calls():
	global calls
	calls += 1


def string_info(text):
	count_calls()
	return len(text), text.upper(), text.lower()


def is_contains(string, list_to_search):
	count_calls()
	lower_str = string.lower()
	lower_list = []

	for item in list_to_search:
		lower_list.append(item.lower())

	if lower_str in lower_list:
		return True
	elif lower_str not in lower_list:
		return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
