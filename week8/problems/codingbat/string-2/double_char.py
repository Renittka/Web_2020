# Given a string, return a string where for every char in the original, there are two chars.
# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'


def double_char(str):
    new_str = ''
    for s in str:
        new_str += s + s
    return new_str


def double_char(str):
    result = ""
    for i in range(len(str)):
        result += str[i] + str[i]
    return result


print(double_char('AAbb'))
