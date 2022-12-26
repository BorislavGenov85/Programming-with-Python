month = input()
night_count = int(input())
room = ""
Studio = ""
Apartment = ""
price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_studio = night_count * 50
    price_apartment = night_count * 65
    if night_count > 14:
        price_studio *= 0.70
    elif night_count > 7:
        price_studio *= 0.95
    if night_count > 14:
        price_apartment *= 0.90

elif month == "June" or month == "September":
    price_studio = night_count * 75.20
    price_apartment = night_count * 68.70
    if night_count > 14:
        price_studio *= 0.80
    if night_count > 14:
        price_apartment *= 0.90

elif month == "July" or month == "August":
    price_studio = night_count * 76
    price_apartment = night_count * 77
    if night_count > 14:
        price_apartment *= 0.90

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
