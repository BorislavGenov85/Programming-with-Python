upper_limit_hundred = int(input())
upper_limit_tens = int(input())
upper_limit_units = int(input())

for i in range(1, upper_limit_hundred + 1):
    for j in range(1, upper_limit_tens + 1):
        for k in range(1, upper_limit_units + 1):
            if k % 2 == 0 and i % 2 == 0:
                if j == 2 or j == 3 or j == 5 or j == 7:
                    print(f"{i} {j} {k}")
