grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stu_list = list(students)
list.sort(stu_list)
stu_grades = {'Vl': 0}
m = len(grades)
i = 0
while i < m:
    j = a = 0
    n = len(grades[i])
    while j < n:
        a = a + grades[i][j]
        j += 1
    a = a / n
    b = stu_list[i]
    stu_grades[b] = a
    i +=1
del stu_grades['Vl']
print('\n', stu_grades)