
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(5, 'str', int)
print_params(5, str)
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [1, 'apple', float]
values_dict = {'a': 2, 'b': bool, 'c': str}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = [':)', 'Работает']

print_params(*values_list_2, '!!!')


