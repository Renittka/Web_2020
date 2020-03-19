# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3. Return n copies of the front;
# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'


def front_times(str, n):
    new_str=''
    for i in range(n):
        if len(str) <= 3:
            new_str += str
        else:
            new_str += str[:3]
    return new_str


print(front_times('Abc', 3))


def front_times(str, n):
    front_len = 3
    if front_len > len(str):
        front_len = len(str)
    front = str[:front_len]

    result = ""
    for i in range(n):
        result = result + front
    return result
