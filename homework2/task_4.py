# test_string: 'apple Banana cherry Apple banana orange'
# output: {'orange': 1, 'apple': 2, 'banana': 2, 'cherry': 1}

user_string = input().lower().split() # Получение строки и создание из нее списка слов, состоящих из букв нижнего регистра.
user_string_keys = set(user_string) # Создание множества для хранения уникальных слов - ключей будущего словаря.
counter_dict_sorted = sorted({key: user_string.count(key) for key in user_string_keys}.items()) # Создание словаря и добавление в него пар "ключ-значение" при использовании полученных во множестве уникальных слов и встроенного метода count() для подсчета значений ключа в списке пользователя. Полученный словарь преобразуется в список кортежей для последующей сортировки по первым значениям, т.е. ключам.
print(dict(counter_dict_sorted)) # Вывод и преобразование отсортированного списка кортежей в словарь.


