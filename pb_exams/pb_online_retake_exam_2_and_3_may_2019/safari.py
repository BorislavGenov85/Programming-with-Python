budget = float(input())
needed_fuel_lt = float(input())
week_day = input()
fuel_price = needed_fuel_lt * 2.10 + 100  # tour guide
if week_day == "Saturday":
    fuel_price *= 0.90
elif week_day == "Sunday":
    fuel_price *= 0.80

diff = abs(budget - fuel_price)
if budget > fuel_price:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
