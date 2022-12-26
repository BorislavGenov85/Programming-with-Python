dog_food_kg = int(input())
input_line = input()
total_food = dog_food_kg * 1000
eaten_food = 0
while input_line != 'Adopted':
    eaten_food_g = int(input_line)

    eaten_food += eaten_food_g

    input_line = input()

if eaten_food <= total_food:
    print(f"Food is enough! Leftovers: {total_food - eaten_food} grams.")
else:
    print(f"Food is not enough. You need {abs(total_food - eaten_food)} grams more.")
   