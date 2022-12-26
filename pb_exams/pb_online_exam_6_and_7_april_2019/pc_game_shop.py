sell_games_count = int(input())

other = 0
game1 = 0
game2 = 0
game3 = 0
for game in range(1, sell_games_count + 1):
    game_name = input()
    if game_name == "Hearthstone":
        game1 += 1
    elif game_name == "Fornite":
        game2 += 1
    elif game_name == "Overwatch":
        game3 += 1
    else:
        other += 1

percent_g1 = game1 / sell_games_count * 100
percent_g2 = game2 / sell_games_count * 100
percent_g3 = game3 / sell_games_count * 100
percent_other = other / sell_games_count * 100
print(f"Hearthstone - {percent_g1:.2f}%")
print(f"Fornite - {percent_g2:.2f}%")
print(f"Overwatch - {percent_g3:.2f}%")
print(f"Others - {percent_other:.2f}%")
