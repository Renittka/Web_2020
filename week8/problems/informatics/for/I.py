# Выведите единственное число - количество делителей числа x.
from math import sqrt
a = int(input())
b = 0
for i in range(1, int(sqrt(a))):
    if a % i == 0:
        b += 1
if sqrt(a).is_integer():
    b = b * 2 + 1
    print(b)
else:
    print(b*2)