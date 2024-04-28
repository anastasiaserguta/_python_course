'''
Пользователь вводит список чисел L. Напишите программу, которая сортирует
список L по возрастанию.
'''

def sort_list(num_list): # Функция сортировки.
    global sorted_list
    if len(num_list) == 0:
        return sorted_list
    minimum = min(num_list)
    sorted_list.append(minimum)
    num_list.remove(minimum)
    return sort_list(num_list)

def for_list(num_list): # Функция, формирующая новый список (на случай, если переданы float-числа).
    list_for_sort = []
    for num in num_list:
        if '.' in num:
            list_for_sort.append(float(num))
        else:
            list_for_sort.append(int(num))

    return sort_list(list_for_sort)


num_list = input('Введите список чисел, разделенных пробелом: ')
sorted_list = []

if '.' in num_list:
    print(for_list(num_list.split()))
else:
    print(sort_list([int(num) for num in num_list.split()]))
