from math import ceil

name = input()
budget = float(input())
beer_count = int(input())
chips_count = int(input())

price_for_one_beer = 1.20

price_for_all_beer = beer_count * price_for_one_beer
price_for_one_chips = price_for_all_beer * 0.45
price_for_all_chips = ceil(price_for_one_chips * chips_count)
total_price = price_for_all_beer + price_for_all_chips
diff = abs(budget - total_price)

if budget >= total_price:
    print(f"{name} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name} needs {diff:.2f} more leva!")



