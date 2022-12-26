budget = int(input())
season = input()
fisherman_count = int(input())

price = 0

if season == "Spring":
    price = 3000
    if fisherman_count >= 12:
        price *= 0.75
    elif 7 <= fisherman_count <= 11:
        price *= 0.85
    elif fisherman_count <= 6:
        price *= 0.90
elif season == "Summer" or season == "Autumn":
    price = 4200
    if fisherman_count >= 12:
        price *= 0.75
    elif 7 <= fisherman_count <= 11:
        price *= 0.85
    elif fisherman_count <= 6:
        price *= 0.90
elif season == "Winter":
    price = 2600
    if fisherman_count >= 12:
        price *= 0.75
    elif 7 <= fisherman_count <= 11:
        price *= 0.85
    elif fisherman_count <= 6:
        price *= 0.90

if (season == "Spring" or season == "Summer" or season == "Winter") and  fisherman_count % 2 == 0:
    price *= 0.95

total_price = abs(price - budget)
if budget >= price:
    print(f"Yes! You have {total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price:.2f} leva.")
