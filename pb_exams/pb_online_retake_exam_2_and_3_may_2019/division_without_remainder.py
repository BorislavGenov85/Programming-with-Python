number_count = int(input())
p1 = 0
p2 = 0
p3 = 0
for i in range(1, number_count + 1):
    current_num = int(input())

    if current_num % 2 == 0:
        p1 += 1
    if current_num % 3 == 0:
        p2 += 1
    if current_num % 4 == 0:
        p3 += 1

p1_percent = p1 / number_count * 100
p2_percent = p2 / number_count * 100
p3_percent = p3 / number_count * 100
print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
