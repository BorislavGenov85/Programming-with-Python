number = int(input())

value1 = 0
value2 = 0

for i in range(1, number + 1):
    current_number = int(input())
    if i % 2 == 0:
        value1 += current_number
    else:
        value2 += current_number

difference = abs(value1 - value2)

if value1 == value2:
    print("Yes")
    print(f"Sum = {value1}")
else:
    print("No")
    print(f"Diff = {difference}")
