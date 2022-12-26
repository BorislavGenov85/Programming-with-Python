import sys

n = int(input())
max_num = -sys.maxsize
sum_num = 0

for i in range(1, n + 1):
    number = int(input())

    sum_num = sum_num + number

    if number > max_num:
        max_num = number

other_sum_num = sum_num - max_num
if max_num == other_sum_num:
    print("Yes")
    print(f"Sum = {other_sum_num}")
else:
    print("No")
    diff = abs(other_sum_num - max_num)
    print(f"Diff = {diff}")


