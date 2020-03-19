# Напишите "функцию голосования" bool Election(bool x, bool y, bool z) , возвращающую то
# значение (true или false), которое среди значений ее аргументов x, y, z встречается чаще.


def election(a):
    co = 0
    ci = 0
    for i in range(len(a)):
        if a[i] == 0:
            co += 1
        else:
            ci += 1
    if ci > co:
        return 1
    else:
        return 0


a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

print(election(a))
