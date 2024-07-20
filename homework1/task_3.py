"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef"."""

user_string = "".join(input().split())

without_repeat = []

for symbol in user_string:
    if symbol not in without_repeat:
        without_repeat.append(symbol)

print("".join(without_repeat))
