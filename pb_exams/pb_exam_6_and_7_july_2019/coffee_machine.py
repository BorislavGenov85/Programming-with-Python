drink = input()
sugar = input()
drink_count = int(input())
price = 0

if drink == "Espresso":
    if sugar == "Without":
        price += drink_count * 0.90
    elif sugar == "Normal":
        price += drink_count * 1
    elif sugar == "Extra":
        price += drink_count * 1.20
elif drink == "Cappuccino":
    if sugar == "Without":
        price += drink_count * 1
    elif sugar == "Normal":
        price += drink_count * 1.20
    elif sugar == "Extra":
        price += drink_count * 1.60
elif drink == "Tea":
    if sugar == "Without":
        price += drink_count * 0.50
    elif sugar == "Normal":
        price += drink_count * 0.60
    elif sugar == "Extra":
        price += drink_count * 0.70

if drink == "Espresso" and drink_count >= 5:
    price *= 0.75

if sugar == "Without":
    price *= 0.65

if price > 15:
    price *= 0.80

print(f"You bought {drink_count} cups of {drink} for {price:.2f} lv.")
