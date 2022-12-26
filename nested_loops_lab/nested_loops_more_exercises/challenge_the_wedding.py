men_count = int(input())
woman_count = int(input())
max_count_table = int(input())
meeting = 0

for i in range(1, men_count + 1):
    for j in range(1, woman_count + 1):
        meeting += 1

        print(f"({i} <-> {j})", end=" ")

        if meeting == max_count_table:
            break
    if meeting == max_count_table:
        break
            