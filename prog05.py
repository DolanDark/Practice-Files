interior_wall = int(input())
exterior_wall = int(input())

if interior_wall:           #checks for true value
    in_wall = []
    for i in range(interior_wall):
        in_wall.append(float(input()))

if exterior_wall:
    ex_wall = []
    for i in range(exterior_wall):
        ex_wall.append(float(input()))

if interior_wall < 0 or exterior_wall < 0:
    print("Invalid Input")
    exit()

if exterior_wall and interior_wall:
    print(f" Total cost {sum(in_wall) * 18 + sum(ex_wall) * 12} INR")

else:
    if exterior_wall:
        print(f" Total cost {sum(ex_wall) * 12} INR")
    elif interior_wall:
        print(f" Total cost {sum(in_wall) * 18} INR")
    else:
        print("Total cost is zero")