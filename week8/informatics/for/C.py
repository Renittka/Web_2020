# Выведите все числа на отрезке от a до b, являющиеся полными квадратами. Если таких чисел нет,
# то ничего выводить не нужно.
from math import sqrt
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if sqrt(i).is_integer():
        print(i)
