day_count = int(input())
total_food = float(input())
dog_food = 0
cat_food = 0
days = 0
biscuits = 0
for day in range(day_count):

    eaten_dog_food = int(input())
    eaten_cat_food = int(input())

    current_day_food = eaten_cat_food + eaten_dog_food

    days += 1
    dog_food += eaten_dog_food
    cat_food += eaten_cat_food

    if days % 3 == 0:
        biscuits += current_day_food * 0.10

eaten_food = cat_food + dog_food
print(f"Total eaten biscuits: {round(biscuits)}gr.")
percent_total = ((dog_food + cat_food) / total_food) * 100
print(f"{percent_total:.2f}% of the food has been eaten.")
percent_dog = (dog_food / eaten_food) * 100
print(f"{percent_dog:.2f}% eaten from the dog.")
percent_cat = (cat_food / eaten_food) * 100
print(f"{percent_cat:.2f}% eaten from the cat.")
