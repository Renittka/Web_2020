# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером).
n = int(input())
a = input().split()
count = 0

for i in range(len(a)):
    a[i] = int(a[i])
    i = 2
for i in range(n):
    if i == n-1:
        print(count)
    elif a[i+1] > a[i]:
        count += 1
