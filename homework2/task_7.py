# Test_string: aaassggfdgksllldfe

user_string = input() + '!' # Добавление к строке символа '!' в качестве условия выхода из цикла.
end_string = '' # Пустой список для внесения полученных значений (путем конкатенации).
total_number = 1 # Счетчик символов.

for i in range(len(user_string)):
    if user_string[i] == '!': # Условие выхода из цикла.
        break
    elif user_string[i] == user_string[i + 1]: # Сравнение и подсчет подряд идущих символов.
        total_number += 1
    else:
        end_string += user_string[i] + str(total_number) 
        total_number = 1

print(end_string)