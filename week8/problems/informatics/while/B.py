# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
from math import pow
a = int(input())
i = 2
while i < a+1:
    if a % i == 0:
        print(i)
        break
    i += 1