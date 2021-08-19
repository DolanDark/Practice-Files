s = str(input())
o = ""
# for i in s:
#     n = int(i)
#     if n > 4:
#         o += str(9-n)
#     else:
#         o += i
# print(i)

for i in s:
    n = int(i)
    o += str(9-n) if n > 4 else i
print(i)