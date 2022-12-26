team_name = input()
played_games = int(input())

total_points = 0
w_count = 0
d_count = 0
l_count = 0
for i in range(1, played_games + 1):

    game_result = input()

    if game_result == "W":
        w_count += 1
    elif game_result == "D":
        d_count += 1
    elif game_result == "L":
        l_count += 1

if played_games > 0:
    total_points = (w_count * 3) + (d_count * 1)
    percents_win_game = (w_count / played_games) * 100
    print(f"{team_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {w_count}")
    print(f"## D: {d_count}")
    print(f"## L: {l_count}")
    print(f"Win rate: {percents_win_game:.2f}%")
else:
    print(f"{team_name} hasn't played any games during this season.")

