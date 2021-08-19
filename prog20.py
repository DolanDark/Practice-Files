keyword = ["break", "case", "continue", "default", "defer", "else", "for",
"func", "goto", "if", "map", "range", "return", "struct", "type", "var"]

word =  input()

if word in keyword:
    print(word, "is a keyword")
else:
    print(word, "is not a keyword")