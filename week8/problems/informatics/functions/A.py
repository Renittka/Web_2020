# Напишите функцию, находящую наименьшее из четырех данных чисел.
def min(a, b):
    if a < b:
        return a
    else:
        return b


a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
print(min(a[0], min(a[1], min(a[2], a[3]))))
