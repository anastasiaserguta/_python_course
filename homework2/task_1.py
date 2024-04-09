words = [word.strip('.,;:-?!').lower() for word in input().split()] # Перебор слов с удаленными знаками препинания из списка, полученного из строки.
print(len(set(words)))