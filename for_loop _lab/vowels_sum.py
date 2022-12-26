text = input()

a = 1
e = 2
i = 3
o = 4
u = 5

value = 0
for _ in text:
    if _ == "a":
        value += 1
    elif _ == "e":
        value += 2
    elif _ == "i":
        value += 3
    elif _ == "o":
        value += 4
    elif _ == "u":
        value += 5
print(value)
