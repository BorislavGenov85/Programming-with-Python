from math import ceil

guest_count = int(input())
budget = float(input())

easter_bread_count = ceil(guest_count / 3)
egg_count = guest_count * 2
easter_bread_price = easter_bread_count * 4
egg_price = egg_count * 0.45
total_price = egg_price + easter_bread_price

diff = abs(budget - total_price)
if total_price <= budget:
    print(f"Lyubo bought {easter_bread_count} Easter bread and {egg_count} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")
