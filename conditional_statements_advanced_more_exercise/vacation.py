budget = float(input())
season = input()

place = ""
price = 0
location = ""

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        price = budget * 0.65
        location = "Alaska"
    elif season == "Winter":
        price = budget * 0.45
        location = "Morocco"
elif budget <= 3000:
    place = "Hut"
    if season == "Summer":
        price = budget * 0.80
        location = "Alaska"
    elif season == "Winter":
        price = budget * 0.60
        location = "Morocco"
elif budget > 3000:
    place = "Hotel"
    if season == "Summer":
        price = budget * 0.90
        location = "Alaska"
    elif season == "Winter":
        price = budget * 0.90
        location = "Morocco"

print(f"{location} - {place} - {price:.2f}")
