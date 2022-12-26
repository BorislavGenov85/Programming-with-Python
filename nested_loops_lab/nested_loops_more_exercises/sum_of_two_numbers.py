start = int(input())
ending = int(input())
magik_num = int(input())
flag = False
count = 0
magik_count = 0
for i in range(start, ending + 1):
    for j in range(start, ending + 1):
        count += 1
        if i + j == magik_num:
            print(f"Combination N:{count} ({i} + {j} = {magik_num})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{count} combinations - neither equals {magik_num}")
