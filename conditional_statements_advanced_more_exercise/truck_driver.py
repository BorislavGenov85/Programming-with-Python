season = input()
km_per_month = float(input())

price_per_km = ""

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.90
    elif season == "Winter":
        price_per_km = 1.05

elif km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.10
    elif season == "Winter":
        price_per_km = 1.25

elif km_per_month <= 20000:
    price_per_km = 1.45

salary = (km_per_month * price_per_km) * 4
salary *= 0.90   #tax
print(f"{salary:.2f}")
