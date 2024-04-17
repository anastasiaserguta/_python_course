'''
Напишите программу - “Игра Жизнь” Джона Конвея.
В игре используется сетка ячеек NxN, где каждая ячейка может быть либо живой, либо мертвой. Игра развивается по шагам (поколениям) на основе набора правил.

Правила:
1. Живая клетка, имеющая < 2 живых соседей, погибает.
2. Живая клетка с 2-3 живыми соседями переходит на следующий шаг.
3. Живая клетка, у которой > 3 живых соседей, погибает.
4. Мертвая клетка, имеющая 3 живых соседа, становится живой на следующем шаге.

Требования:
1. Пользователь указывает размер сетки N.
2. Пользователь вводит число поколений (шагов) M.
3. Программа случайным образом генерирует начальное состояние сетки, в котором каждая ячейка либо жива, либо мертва.
4. Программа меняет начальное состояние на протяжении введенного числа поколений M в соответствии с описанными правилами и выводит каждое поколение на экран.

Комментарии:
В этой задаче вы можете добавлять любые улучшения, которые покажутся вам интересными, сохраняя при этом основные правила.
1. Программа должна работать в терминале.
2. Сетка в игре - это по сути список списков.
3. Для рисования нового поколения поверх старого используйте очистку терминала. Как? Google it 🙂
4. Для передачи параметров (размер сетки, число поколений) в программу используйте либо input(), либо модуль argparse (import argparse) из стандартной библиотеки.
5. Возможность задать время жизни одного поколения (время, в течении которого оно отображается на экране) может быть очень кстати для пользователя. С этим вам может помочь функция sleep() из модуля time
(import time).
'''

from os import system, name
from random import shuffle, randrange
from time import sleep
from copy import deepcopy

print('Добро пожаловать в игру "Жизнь"!')
print('Как Вас зовут?')
user_name = input('Введите имя: ')
print(f'Теперь, {user_name}, необходимо выбрать размер сетки для игры и количество шагов для смены поколений.')
size = int(input('Укажите целое число (больше 8) для определения размера сетки N x N: '))
step = int(input(f'Укажите целое количество шагов для смены поколений на сетке размером {size} x {size}: '))
step_start = step
total_step = 0


dead_cell = '-' # Заполнитель пустых клеток.
live_cell = 'x' # Заполнитель для поколений.
playing_field = [] # Переменная для хранения игрового поля.
playing_field_copy = []
old_gen = [] # Переменные для хранения двух предыдущих поколений.
counter_live_cell = [] # Переменная для хранения значений соседних клеток.
start_gen = 0

def field_generator(size, step): # Основная часть игры - генератор первого и последующих поколений.
    global playing_field_copy, old_gen, total_step
    if name == 'nt':
        system('cls')
    else:
        system('clear')

    print(f'{step}#' * size)
    for row_first_gen in range(size):
        for col_first_gen in range(size):
            print(playing_field[row_first_gen][col_first_gen], end = ' ')
        print()
    sleep(0.7)
    step -= 1

    playing_field_copy = deepcopy(playing_field)

    while step > 0 and playing_field not in old_gen:
        total_step += 1
        old_gen.append(playing_field_copy)
        if name == 'nt':
            system('cls')
        else:
            system('clear')

        for row in range(size):
            for col in range(size):
                counter_live_cell = []

                if playing_field_copy[row][col] == live_cell: # Определяем статус живой клетки на следующем шаге.

                    if row == 0 and col == 0: # [0, 0]
                        counter_live_cell.append(playing_field_copy[row + 1][col])
                        counter_live_cell.append(playing_field_copy[row + 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row][col + 1])
                        if counter_live_cell.count(live_cell) not in [2, 3]:
                            playing_field[row][col] = dead_cell

                    elif row == 0 and col == size - 1: # [0, 5]
                        counter_live_cell.append(playing_field_copy[row][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col])
                        if counter_live_cell.count(live_cell) not in [2, 3]:
                            playing_field[row][col] = dead_cell

                    elif row == size - 1 and col == 0: # [5, 0]
                        counter_live_cell.append(playing_field_copy[row - 1][col])
                        counter_live_cell.append(playing_field_copy[row - 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row][col + 1])
                        if counter_live_cell.count(live_cell) not in [2, 3]:
                            playing_field[row][col] = dead_cell

                    elif row == size - 1 and col == size - 1: # [5, 5]
                        counter_live_cell.append(playing_field_copy[row][col - 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col])
                        if counter_live_cell.count(live_cell) not in [2, 3]:
                            playing_field[row][col] = dead_cell

                    elif col == 0 and row not in [0, size - 1]: # [(1, 2, 3, 4), 0]
                        counter_live_cell.append(playing_field_copy[row + 1][col])
                        counter_live_cell.append(playing_field_copy[row + 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row][col + 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col])
                        if counter_live_cell.count(live_cell) not in [2, 3]:
                            playing_field[row][col] = dead_cell

                    elif col == size - 1 and row not in [0, size - 1]: # [(1, 2, 3, 4), 5]
                        counter_live_cell.append(playing_field_copy[row - 1][col])
                        counter_live_cell.append(playing_field_copy[row - 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col])
                        if counter_live_cell.count(live_cell) not in [2, 3]:
                            playing_field[row][col] = dead_cell

                    elif row == 0 and col not in [0, size - 1]: # [0, (1, 2, 3, 4)]
                        counter_live_cell.append(playing_field_copy[row][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col])
                        counter_live_cell.append(playing_field_copy[row + 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row][col + 1])
                        if counter_live_cell.count(live_cell) not in [2, 3]:
                            playing_field[row][col] = dead_cell

                    elif row == size - 1 and col not in [0, size - 1]: # [5, (1, 2, 3, 4)]
                        counter_live_cell.append(playing_field_copy[row][col - 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col])
                        counter_live_cell.append(playing_field_copy[row - 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row][col + 1])
                        if counter_live_cell.count(live_cell) not in [2, 3]:
                            playing_field[row][col] = dead_cell

                    else: # [(1, 2, 3, 4), (1, 2, 3, 4)]
                        counter_live_cell.append(playing_field_copy[row - 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col])
                        counter_live_cell.append(playing_field_copy[row + 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row][col + 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col])
                        if counter_live_cell.count(live_cell) not in [2, 3]:
                            playing_field[row][col] = dead_cell

                else: # Определяем статус мертвой клетки.

                    if row == 0 and col == 0:
                        counter_live_cell.append(playing_field_copy[row + 1][col])
                        counter_live_cell.append(playing_field_copy[row + 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row][col + 1])
                        if counter_live_cell.count(live_cell) == 3:
                            playing_field[row][col] = live_cell
                            
                    elif row == 0 and col == size - 1:
                        counter_live_cell.append(playing_field_copy[row][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col])
                        if counter_live_cell.count(live_cell) == 3:
                            playing_field[row][col] = live_cell

                    elif row == size - 1 and col == 0:
                        counter_live_cell.append(playing_field_copy[row - 1][col])
                        counter_live_cell.append(playing_field_copy[row - 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row][col + 1])
                        if counter_live_cell.count(live_cell) == 3:
                            playing_field[row][col] = live_cell

                    elif row == size - 1 and col == size - 1:
                        counter_live_cell.append(playing_field_copy[row][col - 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col])
                        if counter_live_cell.count(live_cell) == 3:
                            playing_field[row][col] = live_cell

                    elif col == 0 and row not in [0, size - 1]: # [(1, 2, 3, 4), 0]
                        counter_live_cell.append(playing_field_copy[row + 1][col])
                        counter_live_cell.append(playing_field_copy[row + 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row][col + 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col])
                        if counter_live_cell.count(live_cell) == 3:
                            playing_field[row][col] = live_cell

                    elif col == size - 1 and row not in [0, size - 1]: # [(1, 2, 3, 4), 5]
                        counter_live_cell.append(playing_field_copy[row - 1][col])
                        counter_live_cell.append(playing_field_copy[row - 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col])
                        if counter_live_cell.count(live_cell) == 3:
                            playing_field[row][col] = live_cell
                        
                    elif row == 0 and col not in [0, size - 1]: # [0, (1, 2, 3, 4)]
                        counter_live_cell.append(playing_field_copy[row][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col])
                        counter_live_cell.append(playing_field_copy[row + 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row][col + 1])
                        if counter_live_cell.count(live_cell) == 3:
                            playing_field[row][col] = live_cell

                    elif row == size - 1 and col not in [0, size - 1]: # [5, (1, 2, 3, 4)]
                        counter_live_cell.append(playing_field_copy[row][col - 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col])
                        counter_live_cell.append(playing_field_copy[row - 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row][col + 1])
                        if counter_live_cell.count(live_cell) == 3:
                            playing_field[row][col] = live_cell

                    else:
                        counter_live_cell.append(playing_field_copy[row - 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col - 1])
                        counter_live_cell.append(playing_field_copy[row + 1][col])
                        counter_live_cell.append(playing_field_copy[row + 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row][col + 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col + 1])
                        counter_live_cell.append(playing_field_copy[row - 1][col])
                        if counter_live_cell.count(live_cell) == 3:
                            playing_field[row][col] = live_cell

        for row_next_gen in range(size):
            for col_next_gen in range(size):
                print(playing_field[row_next_gen][col_next_gen], end = ' ')
            print()

        sleep(0.7)

        playing_field_copy = deepcopy(playing_field)
        
        step -= 1
    
    return 'Stop'

if size < 8: # Условие проверки введенного значения. Для своего решения выбрала ограничение для минимального значения в 8 клеток.
    print(f'Выполнение программы остановлено, число {size} меньше 8!')
else:
    first_position_row = list(range(0, size)) # В указанном блоке кода генерируются координаты первого поколения.
    first_position_column = list(range(0, size))
        
    playing_field = [[dead_cell] * size for _ in range(size)] # Разворачиваем пустое игровое поле.
    
    while start_gen <= size:
        start_gen += 1
        shuffle(first_position_row)
        shuffle(first_position_column)
        for i in range(len(first_position_row)):
            playing_field[first_position_row[i]][first_position_column[i]] = live_cell # Размещаем на пустом игровом поле поколения по ранее сгенерированным координатам.

    field_generator(size, step)

    print('Генерация поколений окончена.')

    if playing_field not in old_gen:
        print(f'Это конечное игровое поле размером {size} x {size} с количеством поколений, равных {step_start} шагам.')
    else:
        print(f'Это конечное игровое поле размером {size} x {size} с уникальной генерацией поколений. Генерация остановлена на {total_step} шаге (-ам).')