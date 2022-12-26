budget = float(input())
season = input()

price = 0
rest = ""
destination = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.30
        rest = "Camp"
    elif season == "winter":
        price = budget * 0.70
        rest = "Hotel"
    print(f"Somewhere in {destination}")
    print(f"{rest} - {price:.2f}")

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.40
        rest = "Camp"
    elif season == "winter":
        price = budget * 0.80
        rest = "Hotel"
    print(f"Somewhere in {destination}")
    print(f"{rest} - {price:.2f}")

elif budget > 1000:
    destination = "Europe"
    price = budget * 0.90
    rest = "Hotel"
    print(f"Somewhere in {destination}")
    print(f"{rest} - {price:.2f}")


