num_1_first = int(input())
num_1_second = int(input())
num_2_first = int(input())
num_2_second = int(input())
change = 0
for i in range(num_1_first, 8 + 1):
    for j in range(9, num_1_second, - 1):
        for k in range(num_2_first, 8 + 1):
            for l in range(9, num_2_second, - 1):
                if change == 6:
                    break
                if i % 2 == 0 and k % 2 == 0 and j % 2 != 0 and l % 2 != 0:
                    if j != l or i != k:
                        print(f"{i}{j} - {k}{l}")
                        change += 1
                if i % 2 == 0 and k % 2 == 0 and j % 2 != 0 and l % 2 != 0:
                    if j == l and i == k:
                        print("Cannot change the same player.")



