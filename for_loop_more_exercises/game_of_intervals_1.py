moves = int(input())

total_point = 0
num_to_9 = 0
num_to_19 = 0
num_to_29 = 0
num_to_39 = 0
num_to_50 = 0
invalid = 0
for i in range(1, moves + 1):
    number = int(input())

    if 0 <= number <= 9:
        total_point = total_point + (number * 0.20)
        num_to_9 += 1
    elif 10 <= number <= 19:
        total_point = total_point + (number * 0.30)
        num_to_19 += 1
    elif 20 <= number <= 29:
        total_point = total_point + (number * 0.40)
        num_to_29 += 1
    elif 30 <= number <= 39:
        total_point = total_point + 50
        num_to_39 += 1
    elif 40 <= number <= 50:
        total_point = total_point + 100
        num_to_50 += 1
    elif number > 50 or number < 0:
        total_point = total_point / 2
        invalid += 1

percent_num_to_9 = num_to_9 / moves * 100
percent_num_to_19 = num_to_19 / moves * 100
percent_num_to_29 = num_to_29 / moves * 100
percent_num_to_39 = num_to_39 / moves * 100
percent_num_to_50 = num_to_50 / moves * 100
percent_invalid = invalid / moves * 100

print(f"{total_point:.2f}")
print(f"From 0 to 9: {percent_num_to_9:.2f}%")
print(f"From 10 to 19: {percent_num_to_19:.2f}%")
print(f"From 20 to 29: {percent_num_to_29:.2f}%")
print(f"From 30 to 39: {percent_num_to_39:.2f}%")
print(f"From 40 to 50: {percent_num_to_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
