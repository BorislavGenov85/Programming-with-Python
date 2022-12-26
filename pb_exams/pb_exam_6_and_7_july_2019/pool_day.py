from math import ceil

people = int(input())
entry_tax = float(input())
sun_lounger_tax = float(input())
umbrella_tax = float(input())
price_for_people = people * entry_tax
sun_longer = ceil(people * 0.75)
price_for_sun_lounger = sun_longer * sun_lounger_tax
price_for_umbrella = ceil(people / 2) * umbrella_tax
total_price = price_for_people + price_for_umbrella + price_for_sun_lounger
print(f"{total_price:.2f} lv.")
