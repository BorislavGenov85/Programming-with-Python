drink = input()
sugar = input()
total_drink = int(input())

price = 0
if drink == "Espresso":
    if sugar == "Without":
        price = total_drink * 0.90
    elif sugar == "Normal":
        price = total_drink * 1
    elif sugar == "Extra":
        price = total_drink * 1.20

elif drink == "Cappuccino":
    if sugar == "Without":
        price = total_drink * 1
    elif sugar == "Normal":
        price = total_drink * 1.20
    elif sugar == "Extra":
        price = total_drink * 1.60

elif drink == "Tea":
    if sugar == "Without":
        price = total_drink * 0.50
    elif sugar == "Normal":
        price = total_drink * 0.60
    elif sugar == "Extra":
        price = total_drink * 0.70

if sugar == "Without":
    price = price * 0.65

if drink == "Espresso" and total_drink >= 5:
    price = price * 0.75
if price > 15:
    price = price * 0.80

print(f"You bought {total_drink} cups of {drink} for {price:.2f} lv.")
