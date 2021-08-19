import math

def GETFARE(source,destination):
    route = ["TH","GA","IC","HA","TE","LU","NI","CA"]
    cost = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
    fare = 0.0
    if not(source in route and destination in route):
        print("Invalid Input")
        exit()
    if route.index(source) < route.index(destination):
        for i in range (route.index(source),route.index(destination)+1):      #+1 because we want one away from the initial
            fare += cost[i]
    elif route.index(destination) < route.index(source):
        for i in range(route.index(source)+1, len(route)):
            fare += cost[i]
        for i in range(0,route.index(destination)+1):
            fare += cost[i]
    return float(math.ceil(fare*0.005))

source = input()
destination = input()
fare = GETFARE(source, destination)

if fare == 0:
    print("Invalid Input")
else:
    print("The Fare is - ", fare)