
start_1 = int(input())
start_2 = int(input())
difference_start_1 = int(input())
difference_start_2 = int(input())

for i in range(start_1, (start_1 + difference_start_1) + 1):
    for j in range(start_2, (start_2 + difference_start_2) + 1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and j % 2 != 0 \
                and j % 3 != 0 and j % 5 != 0 and j % 7 != 0:
            print(f"{i}{j}")
