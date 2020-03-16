# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитывает количество положительных чисел среди элементов массива.
n = int(input())
a = input().split()
count = 0

for i in range(len(a)):
    a[i] = int(a[i])

for i in range(n):
    if a[i] > 0:
        count += 1
print(count)