winner_points = 0
movie_count = 0
best_movie = ""
total_points = 0
while True:
    movie = input()

    if movie == "STOP":
        print(f"The best movie for you is {best_movie} with {winner_points} ASCII sum.")
        break

    movie_count += 1

    if movie_count == 7:
        print("The limit is reached.")
        print(f"The best movie for you is {best_movie} with {winner_points} ASCII sum.")
        break

    movie_points = 0
    points = 0

    for char in movie:
        ascii_value = ord(char)

        if "a" <= char <= "z":
            points = ascii_value - (2 * len(movie))
            movie_points += points
        elif "A" <= char <= "Z":
            points = ascii_value - len(movie)
            movie_points += points
        else:
            points = ascii_value
            movie_points += ascii_value

    if movie_points > winner_points:
        winner_points = movie_points
        best_movie = movie
