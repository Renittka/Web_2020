# Подсчитайте и выведите, сколько среди данных N чисел нулей.
n = int(input())
b = 0
for i in range(1, n + 1):
    a = int(input())
    if a == 0:
        b += 1
print(b)