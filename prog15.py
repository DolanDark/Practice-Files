num = int(input())
even = 1
odd = 1
for i in range(1,num+1):
    if i%2==0:
        even *= 3
    else:
        odd *= 2

if num%2==0:
    print(f"{num} term of the expression has value {int(even/3)}")
else:
    print(f"{num} term of the expression has value {int(odd/2)}")
