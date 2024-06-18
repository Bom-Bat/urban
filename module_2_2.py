a = int(input('\n\tВведите первое целое число: '))
b = int(input('\n\tВведите второе целое число: '))
c = int(input('\n\tВведите третье целое число: '))
if a == b and a == c:
    print ('\n\t3 числа равны!')
elif a == b or a == c or b == c:
    print('\n\t2 числа равны!')
else:
    print('\n\t0 чисел равны!')