flour_price_for_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
bark_egg_count = int(input())
packets_of_yeast = int(input())

sugar_price = flour_price_for_kg * 0.75
bark_egg_price = flour_price_for_kg * 1.1
packets_of_yeast_price = sugar_price * 0.20

price_for_flour = flour_price_for_kg * flour_kg
price_for_sugar = sugar_price * sugar_kg
price_for_egg = bark_egg_price * bark_egg_count
price_for_yeast = packets_of_yeast_price * packets_of_yeast

total_price = price_for_flour + price_for_sugar + price_for_egg + price_for_yeast

print(f"{total_price:.2f}")
