immutable_var = 1, 2, 3, 'привет', True, 3.14, [7, 8, 9]
print(immutable_var)

# immutable_var[2] = 0    нельзя, т.к. кортеж неизменяемый
immutable_var[-1][-1] = 10
print(immutable_var)

mutable_list = [1, 2, 3, 4, 5]
mutable_list[0] = 0
print(mutable_list)
