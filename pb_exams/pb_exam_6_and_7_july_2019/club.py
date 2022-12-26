needed_profit = float(input())
cocktail_name = input()
current_profit = 0
price = 0
while cocktail_name != "Party!":
    cocktail_count = int(input())

    price = len(cocktail_name) * cocktail_count
    if price % 2 != 0:
        price *= 0.75

    current_profit += price

    if current_profit >= needed_profit:
        print("Target acquired.")
        break

    cocktail_name = input()

diff = abs(needed_profit - current_profit)
if current_profit < needed_profit:
    print(f"We need {diff:.2f} leva more.")

print(f"Club income - {current_profit:.2f} leva.")
