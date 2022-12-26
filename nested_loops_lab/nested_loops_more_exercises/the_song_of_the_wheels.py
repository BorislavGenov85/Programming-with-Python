control_value = int(input())
count = 0
current_pass = ""

flag = False
for a in range(1, 9 + 1):
    for b in range(1, 9 + 1):
        for c in range(1, 9 + 1):
            for d in range(1, 9 + 1):

                if (a * b) + (c * d) == control_value:
                    if a < b and c > d:
                        if 1 <= a <= 9 and 1 <= b <= 9 and 1 <= c <= 9 and 1 <= d <= 9:
                            print(f"{a}{b}{c}{d}", end=" ")
                            count += 1
                        if count == 4:
                            current_pass = f"{a}{b}{c}{d}"
                            flag = True
print()
if flag:
    print(f'Password: {current_pass}')
else:
    print("No!")
