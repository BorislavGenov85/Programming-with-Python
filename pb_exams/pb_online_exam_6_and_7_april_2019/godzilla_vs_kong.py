budget = float(input())
statists = int(input())
cloth_price_for_one = float(input())

decoration = budget * 0.10
total_cloth_price = statists * cloth_price_for_one
if statists > 150:
    total_cloth_price *= 0.90
total_price = decoration + total_cloth_price

diff = abs(budget - total_price)
if total_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")

