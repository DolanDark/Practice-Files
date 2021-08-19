x = int(input())
y = int(input())

smallest = x if x < y else y
isCoprime = True

for i in range(smallest):
    if i > 1:
        if x % i == 0 and y % i == 0:
            isCoprime = False
            break

print(isCoprime)

# from math import gcd
#
# if gcd(x,y) == 1:
#     print("True")
# else:
#     print("False")