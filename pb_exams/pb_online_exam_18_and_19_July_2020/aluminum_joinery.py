joinery_count = int(input())
type_of_joinery = input()
receiving = input()

joinery_price = 0
if type_of_joinery == "90X130":
    joinery_price = joinery_count * 110
    if joinery_count > 60:
        joinery_price = joinery_price * 0.92
    elif joinery_count > 30:
        joinery_price = joinery_price * 0.95
elif type_of_joinery == "100X150":
    joinery_price = joinery_count * 140
    if joinery_count > 80:
        joinery_price = joinery_price * 0.90
    elif joinery_count > 40:
        joinery_price = joinery_price * 0.94
elif type_of_joinery == "130X180":
    joinery_price = joinery_count * 190
    if joinery_count > 50:
        joinery_price = joinery_price * 0.88
    elif joinery_count > 20:
        joinery_price = joinery_price * 0.93
elif type_of_joinery == "200X300":
    joinery_price = joinery_count * 250
    if joinery_count > 86:
        joinery_price = joinery_price * 0.86
    elif joinery_count > 25:
        joinery_price = joinery_price * 0.91

if receiving == "With delivery":
    joinery_price = joinery_price + 60
elif receiving == "Without delivery":
    joinery_price = joinery_price

if joinery_count > 99:
    joinery_price = joinery_price * 0.96

if joinery_count < 10:
    print("Invalid order")
else:
    print(f"{joinery_price:.2f} BGN")
