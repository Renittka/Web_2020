# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given  scores. Store them in a list and find the score of the runner-up.

n = int(input())
a = input().split()
# a = map(int, input().split())
for i in range(n):
    a[i] = int(a[i])
a.sort()
max = a[n-1]
for i in range(n):
    if max > a[n-i-1]:
        print(a[n-i-1])
        break

