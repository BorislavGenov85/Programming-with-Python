n = int(input())
l = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(97, (l + 97)):
            for m in range(97, (97 + l)):
                for x in range(1, n + 1):
                    if x > i and x > j:
                        print(f"{i}{j}{chr(k)}{chr(m)}{x}", end=" ")
