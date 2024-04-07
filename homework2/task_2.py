# test_string: 1 3 4 3 2 4.0 5.0 3 5

all_nums = input().split()
print('Уникальные числа:', *set(int(float(num)) for num in all_nums))
print('Повторяющиеся числа:', *set(num for num in all_nums if all_nums.count(num) > 1))
print('Четные числа:', *{int(float(num)) for num in all_nums if int(float(num)) % 2 == 0})
print('Нечетные числа:', *{int(float(num)) for num in all_nums if int(float(num)) % 2 != 0})
print('Числа с плавающей точкой:', *[float(num) for num in all_nums if '.' in num])
print('Сумма всех чисел кратных 5:', sum([int(float(num)) for num in all_nums if int(float(num)) % 5 == 0]))
print('Самое большое число:', max(all_nums))
print('Самое маленькое число:', min(all_nums))