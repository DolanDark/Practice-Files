trainee = [[],[],[]]
average = []
for i in range(3):          #defines outerlist
    for j in range(3):      #define inner list
        trainee[i].append(int(input()))
        if trainee[i][-1] not in range(1, 101):
            print("Invalid Input")

print(trainee)

for i in range(3):
    average.append((trainee[0][i]+trainee[1][i]+trainee[2][i]) // 3)

maximum = max(average)

print(maximum)
print(average)

for i in range(3):
    if average[i] < 70:
        print(f"Trainee {i+1} is unfit")
    elif average[i] == maximum:
        print(f"Trainee number {i+1} is selected")
