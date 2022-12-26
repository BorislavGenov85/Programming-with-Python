symbol = input()
c_count = 0
o_count = 0
n_count = 0
word = ""
while True:

    if symbol == "End":
        break

    if symbol == "c":
        c_count += 1
        if c_count == 1:
            pass
        else:
            word += symbol
    elif symbol == "o":
        o_count += 1
        if o_count == 1:
            pass
        else:
            word += symbol
    elif symbol == "n":
        n_count += 1
        if n_count == 1:
            pass
        else:
            word += symbol
    elif "a" <= symbol <= "z" or "A" <= symbol <= "Z":
        word += symbol
    else:
        pass

    if c_count >= 1 and o_count >= 1 and n_count >= 1:
        c_count = 0
        o_count = 0
        n_count = 0
        print(f"{word}", end=" ")
        word = ""

    symbol = input()
