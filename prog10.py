import time
start_timm = time.time()

submenu1 = ["Espresso Coffee", "Cappuccino Coffee", "Latte Coffee"]
submenu2 = ["Plain Tea", "Assam Tea", "Ginger Tea", "Cardamom Tea", "Masala Tea", "Lemon Tea", "Green Tea", "Organic Darjeeling Tea"]
submenu3 = ["Hot and Sour Soup", "Veg Corn Soup", "Tomato Soup", "Spicy Tomato Soup"]
submenu4 = ["Hot Chocolate Drink", "Badam Drink", "Badam-Pista Drink"]

m = input()

if m=="c" or m=="t" or m=="s" or m=="b":
    #val=int(input())
    if m=="c":
        val = int(input())
        if val in range(len(submenu1)):
            print(f"Welcome to CCD \n Enjoy your {submenu1[val-1]}")
        else:
            print("INVALID")

    if m == "t":
        val = int(input())
        if val in range(len(submenu2)):
            print("Welcome to CCD \n Enjoy your {}".format(submenu2[val-1]))
        else:
            print("INVALID")

    if m == "s":
        val = int(input())
        if val in range(len(submenu3)):
            print("Weclome to CCd \n Enjoy your", submenu3[val-1])
        else:
            print("INVALID")

    if m == "b":
        val = int(input())
        if val in range(len(submenu4)):
            print("Welcome to CCD \n Enjoy your", submenu4[val-1])
        else:
            print("INVALID")
else :
    print("Invalid")

print(time.time()-start_timm)