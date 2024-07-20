"""
Даны: три стороны треугольника. Требуется: проверить, действительно ли это
стороны треугольника. Если стороны определяют треугольник, найти его площадь.
Если нет, вывести сообщение о неверных данных.
"""

from decimal import Decimal
from math import sqrt

a, b, c = Decimal(input()), Decimal(input()), Decimal(input())
p = 0
h = 0
S = 0

if a + b > c and b + c > a and c + a > b:
    p = (a + b + c) / 2
    S = sqrt((p * (p - a) * (p - b) * (p - c)))
    print(f"{S:.2f}")
else:
    print("Неверные данные")
