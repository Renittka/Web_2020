# Напишите функцию
# def xor(x, y)
# реализующую функцию "Исключающее ИЛИ" двух логических переменных x и y. Функция Xor должна возвращать true,
# если ровно один из ее аргументов x или y, но не оба одновременно равны true.
def xor(x, y):
    if x == 0 and y == 1 or x == 1 and y == 0:
        return 1
    else:
        return 0


a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

print((xor(a[0], a[1])))
