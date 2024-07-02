def calculate_structure_sum(data_):
    global j
    a = list()
    sum_all = 0
    for i in data_:
        if isinstance(i, list):
            a.extend(i)
        elif isinstance(i, dict):
            a.extend(i.items())
        elif isinstance(i, tuple):
            a.extend(list(i))
        elif isinstance(i, set):
            a.extend(list(i))
        elif isinstance(i, str):
            a.append(len(i))
        elif isinstance(i, float):
            a.append(int(i))
        else:
            a.append(i)
    j += 1
    print(f'\n\tПромежуточный список № {j}: {a}')
    for i in a:
        if not isinstance(i, int):
            a = calculate_structure_sum(a)
            return a
    for i in a:
        sum_all += i
    return sum_all


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
j = 0
result = calculate_structure_sum(data_structure)
print(f'\n\tРезультат сложения чисел списка: {result}')