# Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или
# слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
n = int(input())
value = 1
b = False
if n == 1:
    print("YES")
while value <= n:
    value *= 2
    if value == n:
        b = True
if b is True:
    print("YES")
else:
    print("NO")

