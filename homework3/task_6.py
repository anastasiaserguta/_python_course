'''
Пользователь вводит список чисел L и число N. Числа в списке отсортированы
по возрастанию. Напишите программу, которая осуществляет поиск числа N в
списке L и выводит его индекс, если число найдено, или -1, если числа в списке
нет.
'''
num_list, num_search = sorted(list(map(int, input('Введите список чисел, разделенных пробелом. ').split()))), int(input('Введите число для поиска: '))
search_index = -1
for index in range(len(num_list)):
    if num_list[index] == num_search:
        search_index = index
        break

print(search_index)