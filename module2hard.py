def get_para(num1):
    for i in range(num1 // 2):
        a = i + 1
        num2 = num1 - a
        if a == num2:
            continue
        spis_par.append([a, num2])
    return spis_par


spis_par = []
num = int(input(f'\n\tВведите целое число \n\tв диапазоне от 2 до 20 включительно: '))
i = 2
while i <= num:
    if num % i == 0:
        num1 = i
        res_par = get_para(num1)
    i += 1
print(f'\n\tСписок пар ключей: {res_par}')