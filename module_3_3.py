def print_params(a=1, b='строка', c=True):
    print(a,b,c)


print_params()
print_params(2)
print_params(3,'string')
print_params(4,'string2',False)

print_params(b = 25)  # Работает
print_params(c = [1,2,3])  # Работает

values_list = [1,'str_list',False]
values_dict = {'a': 5,'b': 'str_dict','c': 5.55}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['str_list_2',6]
print_params(*values_list_2,42)  # Работает