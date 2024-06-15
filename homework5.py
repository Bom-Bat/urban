immutable_var = 11, 'string', [17, 14, 27, 18], True, 12, False
print('\nImmutable tuple:', immutable_var)
# Изменения элементов в кортеж не возможны.
immutable_var[2][1] = 104
# Исключение: возможны изменения элементов списка который содержится как элемент кортеж.
print('\nImmutable tuple (c измененным элементом в списке):', immutable_var)
mutable_list = [11, 'slov', 12, False, 7, True]
print('\nMutable list: ', mutable_list)
mutable_list[1] = 5
mutable_list[2] = 'slovo'
mutable_list.append(17)
print('\nMutable list (с изменениями): ', mutable_list)