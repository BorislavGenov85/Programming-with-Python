easter_bread_count = int(input())
bark_with_egg_count = int(input())
cookies_kg = int(input())

easter_bread_price = easter_bread_count * 3.20
bark_with_egg_price = bark_with_egg_count * 4.35
cookies_price = cookies_kg * 5.40
egg_paint = bark_with_egg_count * 12 * 0.15

total_price = easter_bread_price + bark_with_egg_price + cookies_price + egg_paint
print(f"{total_price:.2f}")
