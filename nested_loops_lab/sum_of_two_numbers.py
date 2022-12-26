first_int = int(input())
last_int = int(input())
magick_number = int(input())
combination = 0

flag = False
for x in range(first_int, last_int + 1):
    for y in range(first_int, last_int + 1):
        combination += 1

        if x + y == magick_number:
            print(f"Combination N:{combination} ({x} + {y} = {magick_number})")
            flag = True
            break

    if flag:
        break

if not flag:
    print(f"{combination} combinations - neither equals {magick_number}")
