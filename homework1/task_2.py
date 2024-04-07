'''
Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
'''

word_list = [word.strip('.,;:-?!') for word in input().split()] # Удаление знаков препинания в списке слов.

print(max(word_list, key=len, default='Пустой список')) # Поиск самого длинного слова.