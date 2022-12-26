from math import floor, ceil

tennis_rocket = float(input())
tennis_rocket_count = int(input())
shoes_count = int(input())

tennis_rocket_price = tennis_rocket * tennis_rocket_count
one_shoes_price = tennis_rocket / 6
total_shoes_price = one_shoes_price * shoes_count
price_other = (tennis_rocket_price + total_shoes_price) * 0.2
total_price = tennis_rocket_price + total_shoes_price + price_other
jokovic_price = total_price / 8
sponsor_price = total_price * 7 / 8

print(f"Price to be paid by Djokovic {floor(jokovic_price)}")
print(f"Price to be paid by sponsors {ceil(sponsor_price)}")
