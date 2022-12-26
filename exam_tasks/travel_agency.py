town = input()
package = input()
vip_discount = input()
days = int(input())

towns = ("Bansko", "Borovets", "Varna", "Burgas")
packets = ("withEquipment", "noEquipment", "withBreakfast", "noBreakfast")

if town not in towns or package not in packets:
    print("Invalid input!")
    quit()
if days < 1:
    print("Days must be positive number!")
    quit()

price = 0
if days > 7:
    days -= 1
else:
    days = days
if town == "Bansko" or town == "Borovets":
    if package == "noEquipment":
        price = days * 80
        if vip_discount == "yes":
            price = price * 0.95
    elif package == "withEquipment":
        price = days * 100
        if vip_discount == "yes":
            price = price * 0.90
elif town == "Varna" or town == "Burgas":
    if package == "noBreakfast":
        price = days * 100
        if vip_discount == "yes":
            price = price * 0.93
    elif package == "withBreakfast":
        price = days * 130
        if vip_discount == "yes":
            price = price * 0.88
print(f"The price is {price:.2f}lv! Have a nice time!")
