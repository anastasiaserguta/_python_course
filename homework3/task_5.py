'''
Пользователь вводит положительное целое число N. Напишите программу,
которая генерирует случайный пароль длины N, который содержит символы в
верхнем и нижнем регистрах, числа, и специальные символы: , . * ^ _ ( ) [ ] { } ? !
@.
В пароле должны присутствовать как минимум одна заглавная буква, одна
маленькая буква, одна цифра, и один специальный символ.

!!!!!!!!!!!!!!!!!!!!!!!!
В настоящей программе можно выбрать длину и количество паролей, а также те или иные элементы, которые такие пароль должны включать.
'''
from random import sample # Импортируем необходимый метод для генерации пароля и выхода из программы в случае ввода некорректных значений.
from sys import exit

# Английский алфавит в верхнем/нижнем регистре, цифры и специальные символы.
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_symbols =  '!#$%&*+-=?@^_()[]{{}}'

chars = '' # Переменная для хранения специальных символов.
quantity_pass = int(input('Введите количество паролей для генерации: ')) 
pass_len = int(input('Какое количество символов должен включать пароль: '))

if quantity_pass == 0 or pass_len == 0: # Условие выхода из программы, если введены некорретные данные.
    print('Количество паролей или символов в пароле не может равняться нулю!')
    exit() 

all_answers = [] # Список для хранения ответов пользователя, предполагающих наполнение паролей определенными элементами (по желанию).

for i in range(4):
    if i == 0:
        answer = input('Включать ли цифры (ДА или НЕТ): ').lower()
        if answer == 'да':
            chars += digits
        else:
            all_answers.append(answer)
    elif i == 1:
        answer = input('Включать ли строчные буквы (ДА или НЕТ): ').lower()
        if answer == 'да':
            chars += lowercase_letters
        else:
            all_answers.append(answer)
    elif i == 2:
        answer = input('Включать ли прописные буквы (ДА или НЕТ): ').lower()
        if answer == 'да':
            chars += uppercase_letters
        else:
            all_answers.append(answer)
    elif i == 3:
        answer = input('Включать ли специальные символы (ДА или НЕТ): ').lower()
        if answer == 'да':
            chars += special_symbols
        else:
            all_answers.append(answer)

if all_answers.count('нет') == 4: # Условие выхода из программы при вводе некорректных данных.
    print('Пароль должен состоять из каких-либо символов!') 
    exit()
    
    
answer = input('Исключать ли неоднозначные символы (il1Lo0O) (ДА или НЕТ): ').lower() # Возможность исключения символов, которые не всегда поддаются однозначному прочтению.

if answer == 'да': # Исключаем из сформированной по запросам пользователя строки неоднозначные символы.
    specific_symbol = 'il1Lo0O'
    for j in range(len(specific_symbol)):
        position = chars.find(specific_symbol[j])
        chars = chars[0:position] + chars[(position + 1):]



for _ in range(quantity_pass):
        print(*sample(chars, pass_len), sep = '')
