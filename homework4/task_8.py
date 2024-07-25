'''
Реализуйте функцию merge_sort, которая получает несортированный список, и
сортирует его с помощью алгоритма “сортировка слиянием”.
'''

def merge_parts_of_lists(left, right): # Используем функцию из задачи № 7 для сортировки срезов списка из другой рекурсивной функции.
    
    sorted_list = []
    
    position_1 = 0
    position_2 = 0

    while position_1 < len(left) and position_2 < len(right):
        if left[position_1] < right[position_2]:
            sorted_list.append(left[position_1])
            position_1 += 1
        
        else:
            sorted_list.append(right[position_2])
            position_2 += 1
        

    if position_1 < len(left):
        sorted_list += left[position_1:]
    if position_2 < len(right):
        sorted_list += right[position_2:]

    return sorted_list

def split_and_sort_list(list_for_sort): # Функция, постоянно разделяющая список(срезы списка) на половины. 
    if len(list_for_sort) == 1: # Условие выхода из рекурсии, когда длина передаваемых срезов списка достигнет значения 1.
        return list_for_sort
    middle = len(list_for_sort) // 2
    left = list_for_sort[:middle] # Делим список на половины.
    right = list_for_sort[middle:]
    if len(left) > 1: # Передаем половины для дальйнешего деления обратно в функцию.
        left = split_and_sort_list(left) 
    if len(right) > 1:
        right = split_and_sort_list(right)

    return merge_parts_of_lists(left, right) # При помощи другой функции добавляем в отдельный список элементы от меньшего к большему из полученных на каждом этапе рекурсии срезов списка.


list_for_sort = [int(num) for num in input('Введите список целых чисел, разделенных пробелом: ').split()] # Test: 7 4 67 34 1 4 2 5 7 3 6 4

print(*split_and_sort_list(list_for_sort)) 