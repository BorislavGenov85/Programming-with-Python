name_first_player = input()
name_second_player = input()

first_points = 0
second_points = 0
first_finish_points = 0
second_finish_points = 0

while True:
    first_player_card = input()
    if first_player_card == "End of game":
        print(f"{name_first_player} has {first_points} points")
        print(f"{name_second_player} has {second_points} points")
        break
    second_player_card = input()
    first_player_card = int(first_player_card)
    second_player_card = int(second_player_card)

    if first_player_card > second_player_card:
        first_points += first_player_card - second_player_card
    else:
        second_points += second_player_card - first_player_card

    if first_player_card == second_player_card:
        print("Number wars!")
        first_player_card = int(input())
        second_player_card = int(input())
        if first_player_card > second_player_card:
            first_finish_points = first_points
            print(f"{name_first_player} is winner with {first_finish_points} points")
            break
        else:
            second_finish_points = second_points
            print(f"{name_second_player} is winner with {second_finish_points} points")
            break
