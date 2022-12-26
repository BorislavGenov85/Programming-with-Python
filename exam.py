up_line_first = int(input())
up_line_second = int(input())
up_line_third = int(input())
for i in range(1, up_line_first + 1):
    for j in range(1, up_line_second + 1):
        for k in range(1, up_line_third + 1):
            if i % 2 == 0 and k % 2 == 0:
                if j == 2 or j == 3 or j == 5 or j == 7:
                    print(f"{i} {j} {k}")
