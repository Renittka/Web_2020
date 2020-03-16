# Входные данные
# Вводится целое число, по модулю не превосходящее 10000.
#
# Выходные данные
# Выведите сначала фразу "The next number for the number ", затем введенное число, затем слово " is ", окруженное
# пробелами, затем формулу для следующего за введенным числа, наконец, знак точки без пробела.

a = int(input())
print('The next number for the number ' + str(a) + ' is ' + str(a + 1) + '.')
print('The previous number for the number ' + str(a) + ' is ' + str(a - 1) + '.')