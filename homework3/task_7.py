'''
Решите предыдущую задачу не используя проход по списку в цикле.
'''

num_list, num_search = list(map(int, input('Введите список чисел, разделенных пробелом. ').split())), int(input('Введите число для поиска: '))

if num_search in num_list:
    print(num_list.index(num_search))
else:
    print(-1)