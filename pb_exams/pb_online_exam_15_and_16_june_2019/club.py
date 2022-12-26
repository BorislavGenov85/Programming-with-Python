needed_profit = float(input())
cocktail_name = input()
price = 0
current_price = 0
diff = 0
while True:
    if cocktail_name == "Party!":
        break

    cocktail_count = int(input())

    price = len(cocktail_name) * cocktail_count

    if price % 2 != 0:
        price *= 0.75
    current_price += price

    if current_price >= needed_profit:
        print("Target acquired.")
        break

    cocktail_name = input()

diff = abs(needed_profit - current_price)
if current_price < needed_profit:
    print(f"We need {diff:.2f} leva more.")
print(f"Club income - {current_price:.2f} leva.")
