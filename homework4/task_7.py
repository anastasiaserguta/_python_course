'''
Реализуйте функцию merge_sorted_list, которая принимает два отсортированных
списка, и возвращает новый отсортированный список, содержащий элементы из обоих списков.
'''
# Не совсем поняла условие: нужно самому отсортировать списки перед передачей их в качестве 
# параметров в функцию или мы презюмируем, что они сразу будут отсортированы? 


def sort_any_list(list_1, list_2): # Эта функция принимает любые списки (отсортированные/неотсортированные).
    global sorted_list_1            # Она добавляет минимальное значение из обоих списков в результирующий список и удаляет его из исходных списков.
    if list_1 == [] and list_2 == []:
        return sorted_list_1
    minimum = min(list_1 + list_2)  
    sorted_list_1.append(minimum)
    if minimum in list_1 and minimum in list_2:
        list_1.remove(minimum)
        list_2.remove(minimum)
    elif minimum not in list_1:
        list_2.remove(minimum)
    elif minimum not in list_2:
        list_1.remove(minimum)
    return sort_any_list(list_1, list_2) # Списки с удаленными минимальными значениями передаются обратно в функции для следующей обработки.



def merge_sorted_before_lists(list_1, list_2): # Эта функция для сортировки заранее отсортированных списков (быстрая сортировка).
    sorted_list_2 = [] # Специально созданный список для добавления в него отсортированных элементов.
    
    position_1 = 0 # Определяем исходные значения позиций элементов обоих списков.
    position_2 = 0

    while position_1 < len(list_1) and position_2 < len(list_2): # Устанавливаем условие выхода из цикла до момента, когда проход по одному из списков закончится.
        if list_1[position_1] <= list_2[position_2]: # Конструкция if/else для выбора на каждом проходе цикла наименьшего из двух элементов по соответствующим позициям и добавления его в результирующий список.
            sorted_list_2.append(list_1[position_1])
            position_1 += 1
        
        else:
            sorted_list_2.append(list_2[position_2])
            position_2 += 1

    if position_1 < len(list_1): # Условия, определяющие остаток какого списка добавить в результирующий список отсортированных элементов.
        sorted_list_2 += list_1[position_1:]
    else:
        sorted_list_2 += list_2[position_2:]

    return sorted_list_2

sorted_list_1 = []

list_1 = [int(num) for num in input('Введите 1 список целых чисел, разделенных пробелом.').split()]
list_2 = [int(num) for num in input('Введите 2 список целых чисел, разделенных пробелом.').split()]

# Test: 1 4 2 5 7 3 7 / 4 67 34 6 4 ИЛИ 0 34 45 67 87 132 455 678 / 3 10 11 12 47 57
if input('Введеные списки предварительно отсортированы? Введите: ДА или НЕТ').upper() == 'НЕТ':
    print(sort_any_list(list_1, list_2)) 
else:
    print(merge_sorted_before_lists(list_1, list_2))

