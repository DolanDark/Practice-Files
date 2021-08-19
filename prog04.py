
def caesar(text, key):
    result = ""
    for i in range(len(text)):
        val = text[i]
        if (val.isupper()):
            result += chr((ord(val) + key-65) % 26 + 65)       #for plain text
        if (val.islower()):
            result += chr((ord(val) + key-97) % 26 + 97)        #again,  for plain text
        elif (val.isdigit()):
            result += str(int(val) + key)
        elif (val == "-"):
            result += "-"
        elif (val.isspace()):
            result += " "
    return result

text = input("Enter your plain text - ")
key = int(input("Enter your value - "))

print(caesar(text, key))
