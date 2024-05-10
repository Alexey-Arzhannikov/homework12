def print_params (a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(7, 'is a number - ')
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = [0, False, 'ложь']
value_dict = {'a' : [8, 5, 24], 'b' : 25, 'c' : 'среда'}

print_params(*value_list)
print_params(**value_dict)

value_list_2 = [['5.25', 10.5], 21]
print_params(*value_list_2, 42)