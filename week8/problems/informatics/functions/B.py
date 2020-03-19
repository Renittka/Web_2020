# Напишите функцию double power (double a, int n), вычисляющую значение a^n.
def power(a, n):
    s = 1
    for i in range(n):
        s *= a
    return s


a = input().split()
# for i in range(len(a)):
#     a[i] = int(a[i])

print(int(power(float(a[0]), int(a[1]))))
