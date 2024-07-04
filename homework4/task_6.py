'''
Напишите функцию unique_elements, которая принимает вложенный список и
возвращает уникальные элементы.
'''

list_a = [1, 2, 3, 234, [4, 10, 9], 4], 4, 1, [[234]], 5, 3, [], 4, 10, 9, [8], [4], 5, [6, [7, [], 8, [9]]]


def get_unique_elements(list_a):
    unique = []
    def unpack_list(flat_list):
        for num_list in flat_list:
            if isinstance(num_list, list):
                unpack_list(num_list)
            else:
                unique.append(num_list)
    unpack_list(list_a)
    unique_elements = set(unique)
    return unique_elements

print(*get_unique_elements(list_a))