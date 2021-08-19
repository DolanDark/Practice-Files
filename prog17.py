first = input()
second = input()
third = input()

sep1 = list(first)
sep2 = list(second)


x = len(sep1)
y = len(sep2)

for i in range(x):
    if sep1[i]== "a" or sep1[i]== "e" or sep1[i]== "i" or sep1[i] == "o" or sep1[i] == "u":
        sep1[i] = "%"

#print(sep1)

final_first = "".join(map(str, sep1))
print(final_first)

conso_lower = "bcdfghjklmnpqrstvwxyz"
conso_lower_list = list(conso_lower)
conso_upper = conso_lower.upper()
conso_upper_list = list(conso_upper)

#print(conso_list)
#print(conso_upper)
#print(conso_upper_list)


for i in range(y):
    for j in range(len(conso_lower_list)):
        if sep2[i]==conso_lower_list[j]:
            sep2[i] = "#"

    for k in range(len(conso_upper_list)):
        if sep2[i]==conso_upper_list[k]:
            sep2[i] = "&"

#print(sep2)
final_second = "".join(map(str, sep2))
print(final_second)

final_third = third.upper()
print(final_third)