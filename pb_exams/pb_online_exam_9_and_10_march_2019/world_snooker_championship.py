tour_of_championship = input()
ticket = input()
ticket_count = int(input())
picture_with_trophy = input()

price = 0
discount_photo = False

if tour_of_championship == "Quarter final":
    if ticket == "Standard":
        price += ticket_count * 55.50
    elif ticket == "Premium":
        price += ticket_count * 105.20
    elif ticket == "VIP":
        price += ticket_count * 118.90
elif tour_of_championship == "Semi final":
    if ticket == "Standard":
        price += ticket_count * 75.88
    elif ticket == "Premium":
        price += ticket_count * 125.22
    elif ticket == "VIP":
        price += ticket_count * 300.40
elif tour_of_championship == "Final":
    if ticket == "Standard":
        price += ticket_count * 110.10
    elif ticket == "Premium":
        price += ticket_count * 160.66
    elif ticket == "VIP":
        price += ticket_count * 400

if price > 4000:
    price *= 0.75
    discount_photo = True
elif price > 2500:
    price *= 0.90

if picture_with_trophy == "Y":
    price += ticket_count * 40
    if discount_photo:
        price -= ticket_count * 40

print(f"{price:.2f}")
