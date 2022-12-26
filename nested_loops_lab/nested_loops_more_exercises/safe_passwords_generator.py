a = int(input())
b = int(input())
max_pass = int(input())

count = 0
flag = False
for i in range(35, 55):
    for j in range(64, 96):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                count += 1

                if count > max_pass:
                    flag = True
                    break
                print(f"{chr(i)}{chr(j)}{x}{y}{chr(j)}{chr(i)}", end="|")

                if x == a and y == b:
                    flag = True
                    break
                i += 1
                if i > 55:
                    i = 35
                j += 1
                if j > 96:
                    j = 64
            if flag:
                break
        if flag:
            break
    if flag:
        break
