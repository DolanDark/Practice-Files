def prime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i)==0:
                print(n,"The number is not prime")
                break
        else:
            print(n,"is a prime number")
    else:
        print("1 is neither prime or composite")

num = int(input())
if num > 0:
    prime(num)
else:
    print("please ente rthepsoitive nuber")