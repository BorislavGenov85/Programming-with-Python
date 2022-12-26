strawberries_price = float(input())
banana_kg = float(input())
orange_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberries_price * 0.50
orange_price = raspberries_price * 0.60
banana_price = raspberries_price * 0.20

raspberries_sum = raspberries_kg * raspberries_price
orange_sum = orange_kg * orange_price
banana_sum = banana_kg * banana_price
strawberries_total_price = strawberries_price * strawberries_kg

needed_money = raspberries_sum + orange_sum + banana_sum + strawberries_total_price
print(f"{needed_money:.2f}")
