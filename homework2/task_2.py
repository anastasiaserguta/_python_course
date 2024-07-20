# test_string: 1 3 4 3 2 4.0 5.0 3 5 9.0 9 10 4 3 2 9 4.5 9.3 10.1 10.2 9.0

"""
Пользователь вводит список чисел. Числа вводятся через пробел, могут быть как целые, так и с плавающей точкой. Выведите на экран:
1. Уникальные числа.
2. Повторяющиеся числа.
3. Четные и нечетные чисел.
4. Отрицательные чисел.
5. Числа с плавающей точкой.
6. Сумму всех чисел, кратных 5.
7. Самое большое число.
8. Самое маленькое число
"""

all_nums = [num for num in input().split()]
print("Уникальные числа:", *set(num for num in all_nums))
print("Повторяющиеся числа:", *set(num for num in all_nums if all_nums.count(num) > 1))
print(
    "Четные числа:", *{num for num in all_nums if "." not in num and int(num) % 2 == 0}
)
print(
    "Нечетные числа:",
    *{num for num in all_nums if "." not in num and int(num) % 2 != 0}
)
print("Числа с плавающей точкой:", *[num for num in all_nums if "." in num])
print(
    "Сумма всех чисел кратных 5:",
    sum([int(num) for num in all_nums if "." not in num and int(num) % 5 == 0]),
)

min_max = []
for num in all_nums:
    if "." in num:
        min_max.append(float(num))
    else:
        min_max.append(int(num))

print("Самое большое число:", max(min_max))
print("Самое маленькое число:", min(min_max))
