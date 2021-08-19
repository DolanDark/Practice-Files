n = int(input())

if n == 0:
    print("Time estimate is 0 minutes")
elif n in range(1, 2000):
    print("Time estimate is 25 minutes")
elif n in range(2001,4000):
    print("Time estimate is 35 minutes")
elif n in range(4001, 7000):
    print("Time estimate is 45 minutes")
else:
    print("invalid input")