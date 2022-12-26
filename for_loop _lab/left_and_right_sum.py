number = int(input())

value1 = 0
value2 = 0

for _ in range(number):
    current_number = int(input())
    value1 += current_number
for _ in range(number):
    current_number = int(input())
    value2 += current_number
total_sum = abs(value1 - value2)
if value1 == value2:
    print(f"Yes, sum = {value1}")
else:
    print(f"No, diff = {total_sum}")
