def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(f'\n\tПервая матрица: {result1}')
print(f'\n\tВторая матрица: {result2}')
print(f'\n\tТретья матрица: {result3}')
