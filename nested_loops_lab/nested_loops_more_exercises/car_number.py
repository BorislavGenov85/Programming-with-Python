start_int = int(input())
end_int = int(input())

for i in range(start_int, end_int + 1):
    for j in range(start_int, end_int + 1):
        for k in range(start_int, end_int + 1):
            for l in range(start_int, end_int + 1):
                if i % 2 == 0 and l % 2 != 0 or i % 2 != 0 and l % 2 == 0:
                    if i > l:
                        if (j + k) % 2 == 0:
                            print(f"{i}{j}{k}{l}", end=" ")
