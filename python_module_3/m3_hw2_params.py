# 1
def print_params(a=1, b='строка', c=True):
	print(a, b, c)


print_params()
print_params(0, "fd", False)
print_params(10, c=False, b="fgjkfdj")
print_params(a='da', b=3.5, c=False)

print_params(b=25)
print_params(c=[1, 2, 3])

# 2
values_list = [False, "hi", 22]
values_dict = {'a': True, 'b': "привет", 'c': 1.5}

print_params(*values_list)
print_params(**values_dict)

# 3
values_list_2 = ["hi", (1, 2)]
print_params(*values_list_2, 42)
