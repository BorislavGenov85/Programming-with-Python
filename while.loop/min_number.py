import sys

max_num = sys.maxsize
while True:
    number = input()
    if number == "Stop":
        break
    number = int(number)

    if number <= max_num:
        max_num = number

print(max_num)
