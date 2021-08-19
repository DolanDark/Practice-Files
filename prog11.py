ages = []
fees = 0

for i in range(20):
    m = input()
    if m == "":
        break
    elif int(m) in range(0,120):
        ages.append(int(m))
    else:
        print("INVALID INPUT")

print(ages)

for i in ages:
    if i < 17:
        fees += 200
    elif i < 40:
        fees += 400
    else:
        fees += 300

print("Total Income {}".format(fees))