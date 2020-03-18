# Given the names and grades for each student in a Physics class of  students, store them in a nested list
# and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically and print each
# name on a new line.

arr = []
n = int(input())
for _ in range(0, n):
    arr.append([input(), float(input())])

sec_max = sorted(list(set([marks for name, marks in arr])))[1]
for a, b in sorted(arr):
    if b == sec_max:
        print(a)
