budget = float(input())
category = input()
people_count = int(input())

vip_price = 499.99
normal_price = 249.99
transport = 0
ticket_price = 0
if 1 <= people_count <= 4:
    transport = budget * 0.75
elif people_count <= 9:
    transport = budget * 0.60
elif people_count <= 24:
    transport = budget * 0.50
elif people_count <= 49:
    transport = budget * 0.40
elif people_count >= 50:
    transport = budget * 0.25

if category == "VIP":
    ticket_price = vip_price * people_count
elif category == "Normal":
    ticket_price = normal_price * people_count
price = ticket_price + transport
total_price = abs(budget - price)

if budget > price:
    print(f"Yes! You have {total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price:.2f} leva.")
