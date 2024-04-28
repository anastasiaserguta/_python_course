'''
Решите предыдущую задачу не используя проход по списку в цикле.
'''

num_list, num_search = sorted(list(map(int, input('Введите список чисел, разделенных пробелом. ').split()))), int(input('Введите число для поиска: '))

print(num_list.index(num_search)) if num_search in num_list else print(-1)
