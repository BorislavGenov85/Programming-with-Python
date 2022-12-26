town = input()
package = input()
discount = input()
day = int(input())
price = 0
towns = ("Bansko", "Borovets", "Varna", "Burgas")
packages = ("noEquipment", "withEquipment", "noBreakfast", "withBreakfast")
if day > 7:
    day -= 1
elif day < 1:
    print("Days must be positive number!")
    quit()

if town not in towns or package not in packages:
    print("Invalid input!")
    quit()

if town == "Bansko" or town == "Borovets":
    if package == "noEquipment":
        price += day * 80
        if discount == "yes":
            price *= 0.95
        else:
            price = price
    elif package == "withEquipment":
        price += day * 100
        if discount == "yes":
            price *= 0.90
        else:
            price = price
elif town == "Varna" or town == "Burgas":
    if package == "noBreakfast":
        price += day * 100
        if discount == "yes":
            price *= 0.93
        else:
            price = price
    elif package == "withBreakfast":
        price += day * 130
        if discount == "yes":
            price *= 0.88
        else:
            price = price

print(f"The price is {price:.2f}lv! Have a nice time!")
