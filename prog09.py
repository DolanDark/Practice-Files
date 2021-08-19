n = int(input())
elements = []

for i in range(n):
    dum = list(map(int, input().split()))
    elements.append(dum)

print(elements)