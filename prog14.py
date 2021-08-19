num = int(input())

odd = 0
even = 0

for i in range(1,num+1):    #to staret selection from 1 to n without the 0 issue
    if i%2==0:
        even+=6
    else:
        odd+=7

if num%2==0:
    print("{} term of the series is {}" .format(num, even-6))
else:
    print(f"{num} term of the series is {odd-7}")