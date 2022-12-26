number = int(input())

for i in range(1, 9 + 1):
    for j in range(1, 9 + 1):
        for k in range(1, 9 + 1):
            for l in range(1, 9 + 1):
                if i + j == k + l and number % (i + j) == 0:
                    print(f"{i}{j}{k}{l}", end=' ')
