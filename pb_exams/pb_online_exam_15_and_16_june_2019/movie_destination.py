budget = float(input())
destination = input()
season = input()
day_count = int(input())

price = 0
if destination == "Dubai":
    if season == "Summer":
        price += day_count * 40000
    elif season == "Winter":
        price += day_count * 45000
elif destination == "Sofia":
    if season == "Summer":
        price += day_count * 12500
    elif season == "Winter":
        price += day_count * 17000
elif destination == "London":
    if season == "Summer":
        price += day_count * 20250
    elif season == "Winter":
        price += day_count * 24000

if destination == "Dubai":
    price *= 0.70

if destination == "Sofia":
    price *= 1.25
diff = budget - price
needed_money = abs(budget - price)
if budget > price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {needed_money:.2f} leva more!")
