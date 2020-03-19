# Дан массив, состоящий из целых чисел. Нумерация элементов начинается с 0. Напишите программу, которая выведет элементы
# массива, номера которых четны (0, 2, 4...)
n = int(input())
a = input().split()

for i in range(len(a)):
    a[i] = int(a[i])

for i in range(n):
    if i % 2 == 0:
        print(a[i])
# L = []
# for i in range(n):
#     L.append(int(input()))
#
# for i in range(n):
#     if i % 2 == 0:
#         print(L[i])


