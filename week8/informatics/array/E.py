# Дан массив, состоящий из целых чисел.
# Напишите программу, которая определяет, есть ли в массиве пара соседних элементов с одинаковыми знаками.
n = int(input())
a = input().split()
count = 0
b = False

for i in range(len(a)):
    a[i] = int(a[i])
    i = 2
for i in range(n):
    if i == n-1:
        if b is True:
            print('YES')
        else:
            print('NO')
    elif (a[i+1] > 0 and a[i] > 0) or (a[i+1] < 0 and a[i] < 0):
        b = True
