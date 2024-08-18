import inspect
from pprint import pprint


def introspection_info(obj):
	info = {
		'type': type(obj).__name__,
		'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
		'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
		'module': inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else '__main__',
		'id': id(obj),
		'doc': obj.__doc__
	}

	if isinstance(obj, int):
		info['binary'] = bin(obj)
		info['hex'] = hex(obj)
	elif isinstance(obj, str):
		info['length'] = len(obj)

	return info


if __name__ == '__main__':
	def some_func(x):
		return x


	class SomeClass:
		"""some desc"""

		def __init__(self):
			self.y = 10

		def some_class_func(self):
			return self.y


	number_info = introspection_info(42)
	pprint(number_info)

	print('\n')

	str_info = introspection_info('hello world')
	pprint(str_info)

	print('\n')

	func_info = introspection_info(some_func)
	pprint(func_info)

	print('\n')

	class_info = introspection_info(SomeClass)
	pprint(class_info)

	print('\n')

	module_info = introspection_info(inspect)
	pprint(module_info)

	print('\n')

	type_info = introspection_info(type(0))
	pprint(type_info)

	print('\n')

	list_info = introspection_info([1, 2, 3])
	pprint(list_info)

	print('\n')

	bool_info = introspection_info(False)
	pprint(bool_info)

	print('\n')

	iter_info = introspection_info(iter([1, 2, 3]))
	pprint(iter_info)
