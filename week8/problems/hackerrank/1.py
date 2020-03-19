# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

a = int(input())
if a % 2 != 0:
    print("Weird")
elif a in range(2,6):
    print('Not Weird')
elif a in range(6, 21):
    print('Weird')
else:
    print('Not Weird')
