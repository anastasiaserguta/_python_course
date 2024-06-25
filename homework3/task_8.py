'''
Пользователь вводит список чисел L. Напишите программу, которая сортирует
список L по возрастанию.

строка чисел для теста - 4 7 6 8 9 67 56.0 65.9 43.8 34 90 3 5 7 8
'''
def make_num_list(num_list): # Функция, формирующая новый список (на случай, если переданы float-числа).
    global list_for_sort
    for num in num_list:
        if '.' in num:
            list_for_sort.append(float(num))
        else:
            list_for_sort.append(int(num))
    return list_for_sort

def bubble_sort(num_list, length_list): # Функция пузырьковой сортировки.
    for i in range(length_list - 1):
        for j in range(length_list - 1 - i):
            if num_list[j] > num_list[j + 1]:                  
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

    return num_list

num_list = input('Введите список чисел, разделенных пробелом: ')
length_list = len(num_list.split())
list_for_sort = []

if '.' in num_list:
    list_for_sort = make_num_list(num_list.split())
    print(*bubble_sort(list_for_sort, length_list))
else:
    list_for_sort = [int(num) for num in num_list.split()]
    print(*bubble_sort(list_for_sort, length_list))