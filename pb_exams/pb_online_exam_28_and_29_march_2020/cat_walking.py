min_on_day = int(input())
walk_count = int(input())
calories = int(input())

total_min = walk_count * min_on_day
total_calories = total_min * 5
half_calories = calories / 2

if total_calories >= half_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories}.")
