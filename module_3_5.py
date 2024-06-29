def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


print(f'\n\tВсе равно что Вы введете, главное чтобы были цыфры!')
number_ = input(f'\n\tВведите число : ')
for i in number_:
    if not i.isnumeric():
        number_ = number_.replace(i,'')
number_ = number_.replace('0','')

print(f'\n\tПроизведение цифр введенного числа: {get_multiplied_digits(number_)}')