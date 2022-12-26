import sys

movie_count = int(input())
hi_rating = -sys.maxsize
min_rating = sys.maxsize
rating = 0
total_rating = 0
hi_movie_rating = ""
min_movie_rating = ""

for i in range(1, movie_count + 1):
    movie_name = input()
    rating = float(input())
    total_rating += rating

    if rating > hi_rating:
        hi_rating = rating
        hi_movie_rating = movie_name
    elif rating < min_rating:
        min_rating = rating
        min_movie_rating = movie_name
average = total_rating / movie_count
print(f"{hi_movie_rating} is with highest rating: {hi_rating:.1f}")
print(f"{min_movie_rating} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average:.1f}")

