year = int(input())

if year%4 == 0:
    if year %100 == 0:
        if year%400 == 0:
            print("Not Leap")
        else:
            print("Lepp")
    else:
        print("Leapp Year")
else:
    print("Not Leap")