import m12_calc


def test_add():
	if m12_calc.add(1, 2) == 3:
		print('Test add(a, b) is OK')
	else:
		print('Test add(a, b) failed')


def test_sub():
	if m12_calc.sub(3, 2) == 1:
		print('Test sub(a, b) is OK')
	else:
		print('Test sub(a, b) failed')


def test_mul():
	if m12_calc.mul(2, 2) == 4:
		print('Test mul(a, b) is OK')
	else:
		print('Test mul(a, b) failed')


def test_div():
	if m12_calc.div(9, 3) == 3:
		print('Test div(a, b) is OK')
	else:
		print('Test div(a, b) failed')


test_add()
test_sub()
test_mul()
test_div()
