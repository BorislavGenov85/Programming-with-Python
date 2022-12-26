movie_name = input()
day_count = int(input())
ticket_count = int(input())
ticket_price = float(input())
cinema_percent = int(input())

price_per_day = ticket_count * ticket_price
price_for_all_period = day_count * price_per_day
price_for_cinema = price_for_all_period * cinema_percent / 100
total_price = price_for_all_period - price_for_cinema

print(f"The profit from the movie {movie_name} is {total_price:.2f} lv.")
