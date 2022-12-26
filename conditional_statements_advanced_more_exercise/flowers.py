chrysanthemum_count = int(input())
roses_count = int(input())
tulip_count = int(input())
season = input()
holiday = input()
arrangement = 2

price = 0
total_flower_count = chrysanthemum_count + roses_count + tulip_count
if season == "Spring" or season == "Summer":
    chrysanthemum_price = chrysanthemum_count * 2
    roses_price = roses_count * 4.10
    tulip_price = tulip_count * 2.50
    price = chrysanthemum_price + roses_price + tulip_price
    if holiday == "Y":
        price *= 1.15
    if tulip_count > 7 and season == "Spring":
        price *= 0.95
    if total_flower_count > 20:
        price *= 0.80

elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = chrysanthemum_count * 3.75
    roses_price = roses_count * 4.50
    tulip_price = tulip_count * 4.15
    price = chrysanthemum_price + roses_price + tulip_price
    if holiday == "Y":
        price *= 1.15
    if roses_count >= 10 and season == "Winter":
        price *= 0.90
    if total_flower_count > 20:
        price *= 0.80

total_price = price + arrangement
print(f"{total_price:.2f}")
