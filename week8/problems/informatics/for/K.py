# Вводится число N, а затем N чисел, сумму которых необходимо вычислить.
n = int(input())
sum = 0
for i in range(1, n+1):
    b = int(input())
    sum += b
print(sum)