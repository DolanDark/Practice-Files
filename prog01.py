n = int(input())
for i in range (n):
    name = input()
    l = name.split(",")
    try:
        print(name.split(',')[1].strip())
    except:
        print("N/A")
