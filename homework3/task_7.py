'''
Пользователь вводит список чисел L и число N. Числа в списке отсортированы
по возрастанию. Напишите программу, которая осуществляет поиск числа N в
списке L и выводит его индекс, если число найдено, или -1, если числа в списке
нет.

Решите предыдущую задачу не используя проход по списку в цикле.
'''

num_list, num_search = sorted(list(map(int, input('Введите список чисел, разделенных пробелом. ').split()))), int(input('Введите число для поиска: '))

first_index = 0
last_index = len(num_list) - 1
middle_index = len(num_list) // 2

while num_list[middle_index] != num_search and first_index <= last_index:
    if num_search > num_list[middle_index]:
        first_index = middle_index + 1
    else:
        last_index = middle_index - 1
    middle_index = (first_index + last_index) // 2

if first_index > last_index:
    print('-1')
else:
    print(middle_index)

