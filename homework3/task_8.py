'''
Пользователь вводит список чисел L. Напишите программу, которая сортирует
список L по возрастанию.
'''

def sort_integer(num_list): # Для списка целых чисел.
    print(*sorted(list(map(int, num_list))))

def sort_float_and_integer(num_list): # Для списка любых чисел.
    new_num_list = []
    for num in num_list:
        if '.' in num:
            new_num_list.append(float(num))
        else:
            new_num_list.append(int(num))

    print(*sorted(new_num_list))


num_list = input('Введите список чисел, разделенных пробелом: ')

if '.' in num_list:
    sort_float_and_integer(num_list.split())
else:
    sort_integer(num_list.split())
