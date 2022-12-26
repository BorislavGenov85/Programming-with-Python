needed_height = int(input())

lath_height = needed_height - 30
unsuccessful_jump = 0
all_jumps = 0
flag = False
while unsuccessful_jump != 3:
    jump_height = int(input())

    if jump_height > lath_height:
        lath_height += 5
        unsuccessful_jump = 0
    else:
        unsuccessful_jump += 1

    all_jumps += 1

    if jump_height > needed_height:
        flag = True
        break
if flag:
    print(f"Tihomir succeeded, he jumped over {needed_height}cm after {all_jumps} jumps.")
else:
    print(f"Tihomir failed at {lath_height}cm after {all_jumps} jumps.")
