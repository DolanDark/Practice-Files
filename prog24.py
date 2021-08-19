n = int(input())
low = 0
idx = 1
for i in range(n):
    x, y = [int(j) for j in input().split()]
    val = x * y
    if i == 0:
        low(val)
    if val < idx:
        idx = i + 1
        low = val

print(idx)

