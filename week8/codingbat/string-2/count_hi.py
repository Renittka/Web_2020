# Return the number of times that the string "hi" appears anywhere in the given string.
# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2


def count_hi(str):
    new_str = ''
    count = 0
    for i in range(0, len(str)-1):
        new_str = str[i] + str[i+1]
        if new_str == 'hi':
            count += 1
    return count


def count_hi(str):
    sum = 0
    for i in range(len(str)-1):
        if str[i:i+2] == 'hi':
            sum = sum + 1
    return sum


print(count_hi('hihi'))
