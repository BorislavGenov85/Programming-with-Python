movie = input()
paket = input()
tickets = int(input())

price = 0

if movie == "John Wick":
    if paket == "Drink":
        price += tickets * 12
    elif paket == "Popcorn":
        price += tickets * 15
    elif paket == "Menu":
        price += tickets * 19

elif movie == "Star Wars":
    if paket == "Drink":
        price += tickets * 18
    elif paket == "Popcorn":
        price += tickets * 25
    elif paket == "Menu":
        price += tickets * 30
elif movie == "Jumanji":
    if paket == "Drink":
        price += tickets * 9
    elif paket == "Popcorn":
        price += tickets * 11
    elif paket == "Menu":
        price += tickets * 14

if movie == "Star Wars" and tickets >= 4:
    price *= 0.70
if movie == "Jumanji" and tickets == 2:
    price *= 0.85

print(f"Your bill is {price:.2f} leva.")
