destination = input()
date = input()
nights_count = int(input())

price = 0
if destination == "France":
    if date == "21-23":
        price += nights_count * 30
    elif date == "24-27":
        price += nights_count * 35
    elif date == "28-31":
        price += nights_count * 40
elif destination == "Italy":
    if date == "21-23":
        price += nights_count * 28
    elif date == "24-27":
        price += nights_count * 32
    elif date == "28-31":
        price += nights_count * 39
elif destination == "Germany":
    if date == "21-23":
        price += nights_count * 32
    elif date == "24-27":
        price += nights_count * 37
    elif date == "28-31":
        price += nights_count * 43

print(f"Easter trip to {destination} : {price:.2f} leva.")
