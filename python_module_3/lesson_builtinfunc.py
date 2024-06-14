a = [1, 1, 1]
b = ''

print(all(a))
print(dir(a))
print(type(b))
print(isinstance(b, str))

d = [1, 1, 1]
c = d
c[0] = 2
print(c)
print(d)
print(id(a))
print(id(d))
print(id(c))
print(c is d)


def helper():
	"""
	Эта функция-помощник
	"""
	pass


print(helper.__doc__)


print(help(print))
