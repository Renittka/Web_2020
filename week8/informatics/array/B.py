# Дан массив, состоящий из целых чисел. Напишите программу, которая выводит те элементы массива,
# которые являются чётными числами.
n = int(input())
a = input().split()

for i in range(len(a)):
    a[i] = int(a[i])

for i in range(n):
    if a[i] % 2 == 0:
        print(a[i])
