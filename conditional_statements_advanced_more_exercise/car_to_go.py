budget = float(input())
season = input()
car_class = ""
car = ""

price = 0
if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        car = "Jeep"
        price = budget * 0.65
elif budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        car = "Jeep"
        price = budget * 0.80
elif budget > 500:
    car_class = "Luxury class"
    car = "Jeep"
    price = budget * 0.90

print(f"{car_class}")
print(f"{car} - {price:.2f}")
