# Выведите все точные квадраты натуральных чисел, не превосходящие данного числа N.
from math import pow
n = int(input())
i = 1
while pow(i, 2) < n+1:
    print(int(pow(i, 2)))
    i += 1