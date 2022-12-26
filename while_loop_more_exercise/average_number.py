number = int(input())
total = 0
for i in range(1, number + 1):
    current_num = int(input())
    total += current_num

average = total / number
print(f"{average:.2f}")
