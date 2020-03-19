# Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами.
from math import sqrt
a = int(input())
b = int(input())
c = sqrt(pow(a, 2) + pow(b, 2))
print(c)