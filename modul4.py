from fake_math import divide as divf
from true_math import divide as divt


first = float(input('\n\tВведите первое число: '))
second = float(input('\n\tВведите второе число: '))
var = int(input('\n\tКаким способом будем расчитывать? \n\t1-школа \n\tдругая цифра - высшая матиматика: '))
if var == 1:
    print(f'\n\tРезультат из школы: {divf(first, second)}')
else:
    print(f'\n\tРезультат из вычшей матиматики: {divt(first, second)}')