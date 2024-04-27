'''
Напишите функцию unique_elements, которая принимает вложенный список и
возвращает уникальные элементы.
'''

list_a = [1, 2, 3, 234, [4, 10, 9], [[234]], 5, 3, [], 4, 10, 9, [8], [4], 5, [6, [7, [], 8, [9]]]]


def unique_elements(list_a):
    global uni_elements
    if list_a == []: # Условие выхода из рекурсии, когда обрабатываемый через срезы список станет пустым.
        return list_a 
    if isinstance(list_a[0], list): # Проверяем переданный функции список(срез списка) на соответствие типу для его последующей передачи в эту же функцию для распаковки.
        return unique_elements(list_a[0]) + unique_elements(list_a[1:])
    if isinstance(list_a[0], int) and list_a[0] not in uni_elements: # Собираем уникальные значения в специально созданном списке.
        uni_elements.append(list_a[0])        

    return list_a[:1] + unique_elements(list_a[1:]) # "Срезаем" обработанную часть списка и передаем функции оставшуюся часть списка для следующей обработки.



uni_elements = []

unique_elements(list_a)

print(*uni_elements) # Сделать возврат списка из функции у меня не получилось....