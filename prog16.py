num = int(input())

even = 0
odd = 0

for i in range(1, num+1):
    if i%2==0:
        even+=1
    else:
        odd+=2

if num%2==0:
    print(f"{num} term of the expression is {even-1}")
else:
    print(f"{num} term of the expression is {odd-2}")