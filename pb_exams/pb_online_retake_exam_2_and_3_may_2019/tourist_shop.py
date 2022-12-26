budget = float(input())
product_name = input()
product_count = 0
price = 0
while product_name != "Stop":
    product_price = float(input())

    product_count += 1
    if product_count % 3 == 0:
        price += product_price / 2
        if price > budget:
            diff = abs(budget - price)
            print("You don't have enough money!")
            print(f"You need {diff:.2f} leva!")
            break
    else:
        price += product_price
        if price > budget:
            diff = abs(budget - price)
            print("You don't have enough money!")
            print(f"You need {diff:.2f} leva!")
            break
    product_name = input()
else:
    print(f"You bought {product_count} products for {price:.2f} leva.")
