game_count = int(input())

first_game = 0
second_game = 0
third_game = 0
other_game = 0
for i in range(1, game_count + 1):
    game = input()

    if game == "Hearthstone":
        first_game += 1
    elif game == "Fornite":
        second_game += 1
    elif game == "Overwatch":
        third_game += 1
    else:
        other_game += 1

percent_first_game = (first_game / game_count) * 100
percent_second_game = (second_game / game_count) * 100
percent_third_game = (third_game / game_count) * 100
percent_other = (other_game / game_count) * 100
print(f"Hearthstone - {percent_first_game:.2f}%")
print(f"Fornite - {percent_second_game:.2f}%")
print(f"Overwatch - {percent_third_game:.2f}%")
print(f"Others - {percent_other:.2f}%")
