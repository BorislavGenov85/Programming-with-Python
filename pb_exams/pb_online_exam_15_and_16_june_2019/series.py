budget = float(input())
serial_count = int(input())

total_price = 0
for i in range(1, serial_count + 1):
    name = input()
    price = float(input())

    if name == "Thrones":
        total_price += price * 0.50
    elif name == "Lucifer":
        total_price += price * 0.60
    elif name == "Protector":
        total_price += price * 0.70
    elif name == "TotalDrama":
        total_price += price * 0.80
    elif name == "Area":
        total_price += price * 0.90
    else:
        total_price += price

dif = abs(budget - total_price)
if budget >= total_price:
    print(f"You bought all the series and left with {dif:.2f} lv.")
else:
    print(f"You need {dif:.2f} lv. more to buy the series!")
