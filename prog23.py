x = int(input())
bin = str(bin(x))[2:]
total = 0

for i in bin:
    total += int(i)

print(total)