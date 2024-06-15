example = 'Длинношеее с длинной шеей'
print('\n')
print(example[0], '\n')
print(example[-1], '\n')
l = len(example)
a = l / 2
b = int(a) + 1 if (int(a) % 2) != 0 else int(a)
c = int(b) - 1 if (l % 2) == 0 and (b % 2) == 0 else int(b)
print(example[c:], '\n')
print(example[::-1], '\n')
print(example[1::2], '\n')