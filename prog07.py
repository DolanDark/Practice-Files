n = int(input())
k = int(input())
j = int(input())
m = int(input())
p = int(input())

if (n or k or j or m or p) < 0:
    print("invalid output")
else:
    if (k>0):
        ate_banana=float(m/k)
    if (j>0):
        ate_peanut=float(p/j)
    n = n - ate_banana - ate_peanut
    print("Number of monkys left in the tree", n)
