'''Напишите программу, которая предлагает пользователю угадать число N,
сгенерированное случайно в диапазоне от 0 до 100. Когда пользователь вводит
ответ, программа должна дать ему подсказку, если введенное число больше
или меньше N. Программа должна давать пользователю 5 попыток.

!!!!!!!!!!!!!!!
Данная программа в дополнениее к условию позволяет выбрать диапазон значений для игры.
'''

from random import randint # Импортируем функцию для получения случайного числа.

def start_game():    # Функция старта, где пользователь определяет некоторые условия игры.
    print(f'{name}, введите диапазон чисел.')
    start_num = int(input('От числа: '))
    end_num = int(input('До числа: '))
    num_random = randint(start_num, end_num) # Загадываем число.

    print(f'Теперь, {name}, попробуйте угадать случайное число.')
    print(f'{name}, необходимо ввести любое целое число от {start_num} до {end_num}.')

    digit_user = int(input('Введите предполагаемое число: ')) 

    if digit_user < start_num or digit_user > end_num:
        is_valid(start_num, end_num, digit_user, num_random)
    else:
        random_game(start_num, end_num, digit_user, num_random)

def is_valid(start_num, end_num, digit_user, num_random): # Функция проверки корректности введенного пользователем числа.
        flag = False
        while flag != True:
            if digit_user < start_num or digit_user > end_num:
                print(f'{name}, введите корректное число (в диапазоне от {start_num} до {end_num} включительно).')
                digit_user = int(input())
                
            else:
                flag = True
                break
                
        if flag == True: # При вводве корректного значения запускаем основной блок игры.
            random_game(start_num, end_num, digit_user, num_random)

def random_game(start_num, end_num, digit_user, num_random):   # Основая часть игры.                              
    total = 1
    while num_random != digit_user and total != 5:
    
        if digit_user > num_random:
            print(f'{name}, многовато, попробуйте еще раз:(')
            digit_user = int(input('Введите новое число: '))
            total += 1
        elif digit_user < num_random:
            print(f'{name}, маловато, попробуйте еще раз.')
            digit_user = int(input('Введите новое число: '))
            total += 1
        
    if digit_user == num_random:
        print(f'{name}, Вы угадали за {total} попыток поздравляем!')
        print(f'Спасибо, {name}, что играли в числовую угадайку. Еще увидимся...')
    else:
        print(f'{name}, закончились попытки. Вы проиграли:(')
        print(f'Загаданное число - {num_random}.')

print('Добро пожаловать в числовую угадайку!')
name = input('Как Вас зовут? ')
start_game()

answer = input('Желаете начать сначала? Введите ДА или НЕТ ').lower() # Повторный запуск игры (при необходимости).

if answer == 'да':
    start_game()
else:
    print(f'{name}, cпасибо за игру! До свидания!')
