'''
Пользователь вводит положительное целое число N. Напишите программу,
которая выводит на экран последовательность Фибоначчи до числа N. Число N
не обязательно является числом последовательности, так что нужно вывести
на экран числа последовательности, которые меньше либо равны N.
'''

num = int(input('Введите целое положительное число: '))
subseq = [0, 1]
while subseq[-1] + subseq[-2] <= num:
    subseq.append(subseq[-1] + subseq[-2])

print(*subseq)