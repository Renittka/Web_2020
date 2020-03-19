# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the
# types listed above. Iterate through each command in order and perform the corresponding operation on your list.

a = []
N = int(input())
for n in range(N):
    x = input().split()
    command = x[0]
    if command == 'insert':
        a.insert(int(x[1]), int(x[2]))
    if command == 'print':
        print(a)
    if command == 'remove':
        a.remove(int(x[1]))
    if command == 'append':
        a.append(int(x[1]))
    if command == 'sort':
        a.sort()
    if command == 'pop':
        if len(a) != 0:
            a.pop()
    if command == 'reverse':
        a.reverse()

