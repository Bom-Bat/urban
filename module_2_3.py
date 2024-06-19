my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = len(my_list)
i = -1
while i < a:
    i +=1
    if i == a:
        break
    if my_list[i] > 0:
        print(f'\n\tЧисло {my_list[i]} положительное')
    elif my_list[i] == 0:
        continue
    else:
        print('\n\tВстретили отрицательное число \n\n\t\tС Т О П !')
        break
print('\n\tРасчет окончен')
