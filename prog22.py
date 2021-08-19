import string as S
n = input()
print("".join(["".join(map(chr, range(65 if x in S.ascii_uppercase else 97 if x in S.ascii_lowercase else 48, ord(x) + 1))) for x in n]))