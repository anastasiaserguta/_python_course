'''
Пользователь вводит две матрицы чисел A и В. Напишите программу, которая
производит сложение матриц и выводит результат на экран. Матрицы имеют
одинаковый размер.
'''

n, m = map(int, input('Введите размеры матрицы в формате двух чисел, разделенных пробелом. ').split()) # Ввод размера матриц n x m.

matrix1 = [] 
matrix2 = []

for i in range(1, n + 1):
    matrix1.append(input(f'Введите {i} строку чисел, разделенных пробелами, для формирования матрицы № 1, состоящей из {n} строк и {m} столбцов: ').split()) # Считывание первой матрицы по вводимым пользователем спискам чисел, разделенных пробелами.

for j in range(1, n + 1):
    matrix2.append(input(f'Введите {j} строку чисел, разделенных пробелами, для формирования матрицы № 2, состоящей из {n} строк и {m} столбцов: ').split()) # Считывание второй матрицы по вводимым пользователем спискам чисел, разделенных пробелами.

for k in range(n):
    for l in range(m):
        print(int(matrix1[k][l]) + int(matrix2[k][l]), end = ' ') # Сложение матриц.
    print()