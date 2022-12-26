from math import ceil, floor

day_count = int(input())
food_in_kg = float(input())
first_deer_food_per_day_kg = float(input())
second_deer_food_per_day_kg = float(input())
third_deer_food_per_day_kg = float(input())

first_deer = first_deer_food_per_day_kg * day_count
second_deer = second_deer_food_per_day_kg * day_count
third_deer = third_deer_food_per_day_kg * day_count
needed_food = first_deer + second_deer + third_deer

diff = abs(food_in_kg - needed_food)
if needed_food < food_in_kg:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')

