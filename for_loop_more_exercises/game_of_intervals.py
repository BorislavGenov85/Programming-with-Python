moves = int(input())

total_numbers_to_9 = 0
total_numbers_to_19 = 0
total_numbers_to_29 = 0
total_numbers_to_39 = 0
total_numbers_to_50 = 0
total_invalid_num = 0
total_points = 0
for i in range(1, moves + 1):
    number = int(input())

    points_count = 0
    numbers_to_9 = 0
    numbers_to_19 = 0
    numbers_to_29 = 0
    numbers_to_39 = 0
    numbers_to_50 = 0
    invalid_num = 0
    if 0 <= number <= 9:
        points_count += number * 0.20
        numbers_to_9 += 1
    elif 10 <= number <= 19:
        points_count += number * 0.30
        numbers_to_19 += 1
    elif 20 <= number <= 29:
        points_count += number * 0.40
        numbers_to_29 += 1
    elif 30 <= number <= 39:
        points_count += 50
        numbers_to_39 += 1
    elif 40 <= number <= 50:
        points_count += 100
        numbers_to_50 += 1
    elif 0 > number > 50:
        points_count = points_count / 2
        invalid_num += 1

    total_points += points_count
    total_numbers_to_9 += numbers_to_9
    total_numbers_to_19 += numbers_to_19
    total_numbers_to_29 += numbers_to_29
    total_numbers_to_39 += numbers_to_39
    total_numbers_to_50 += numbers_to_50
    total_invalid_num += invalid_num
percent_total_num_to_9 = total_numbers_to_9 / moves * 100
percent_total_num_to_19 = total_numbers_to_19 / moves * 100
percent_total_num_to_29 = total_numbers_to_29 / moves * 100
percent_total_num_to_39 = total_numbers_to_39 / moves * 100
percent_total_num_to_50 = total_numbers_to_50 / moves * 100
percent_total_invalid_num = total_invalid_num / moves * 100
print(f"{total_points:.2f}")
print(f"From 0 to 9: {percent_total_num_to_9:.2f}%")
print(f"From 10 to 19: {percent_total_num_to_19:.2f}%")
print(f"From 20 to 29: {percent_total_num_to_29:.2f}%")
print(f"From 30 to 39: {percent_total_num_to_39:.2f}%")
print(f"From 40 to 50: {percent_total_num_to_50:.2f}%")
print(f"Invalid numbers: {percent_total_invalid_num:.2f}%")
