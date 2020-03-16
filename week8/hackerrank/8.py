# Given the names and grades for each student in a Physics class of  students, store them in a nested list
# and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically and print each
# name on a new line.
# n = int(input())
# a = {}
# for i in range(n):
#     a[]
#     a[i] = int(a[i])
# a.sort()
# max = a[n-1]
# for i in range(n):
#     if max > a[n-i-1]:
#         print(a[n-i-1])
#         break
marksheet = []
for _ in range(0, int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))
for a, b in sorted(marksheet):
    if b == second_highest:
        print(a)
