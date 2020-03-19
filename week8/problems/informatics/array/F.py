# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.

s = input()
arr = list(map(int, (input()).split()))
n = len(arr)
c = 0
for i in range(1, n-1):
    if (arr[i] > arr[i-1]) & (arr[i] > arr[i+1]):
        c += 1
print(c)

# n = int(input())
# a = input().split()
# count = 0
#
# for i in range(len(a)):
#     a[i] = int(a[i])
#     i = 2
# for i in range(n-1):
#     if i == n-1:
#         print(count)
#     elif (a[i] > a[i-1]) and (a[i] > a[i+1]):
#         count += 1