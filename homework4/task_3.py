'''
Напишите декоратор log_calls, который записывает в файл время вызова, имя и
аргументы вызванной функции. Один вызов функции - одна строка в файле.
Декоратор должен принимать имя файла как параметр.
'''

from datetime import datetime # Импортируем функции для получения значений текущего времени и одного случайного числа из заданного диапазона.
from random import randint 

def log_calls(func): # Декоратор, в который передается имя файла, функция, ее время вызова и аргументы. 
    def wrapper(file, *args):
        result = func(file, *args)
        data = f"Function name: {func.__name__}. Start time: {datetime.now()}. Arguments: {args}. Result: {result}." # Собираем строку в соответствии с условием для добавления в файл.
        file.write(data + '\n') # Добавляем значения в файл.
        file.close() 
        return result
    return wrapper    


@log_calls
def random_element(file, start, end): # Функция вывода случайного числа из заданного пользователем диапазона.
    return randint(start, end)

start = 0
end = 0

for _ in range(10): # Цикл для ввода значений, передаваемых в функцию.
    print('Для вывода случайного числа введите диапазон')
    start, end = int(input('ОТ числа: ')), int(input('ДО числа: '))
    if start > end:
        print('Стартовое значение должно быть меньше предельного!')
    else:
        fh = open('log_file.txt', 'a')
        print(random_element(fh, start, end))

fh = open('log_file.txt') # Читаем файл.
print(fh.read())

