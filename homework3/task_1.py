'''
Задача 1
Пользователь вводит положительное целое число N. Напишите программу, которая считает факториал N.
'''

from math import factorial as f
num = int(input('Введите положительное целое число: '))
print(f'Факториал числа {num} равен {f(num)}.')