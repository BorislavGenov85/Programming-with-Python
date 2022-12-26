day_count = int(input())

total_money = 0
most_win = 0
for days in range(1, day_count + 1):

    sport = input()
    money = 0
    win_game = 0
    loose_game = 0
    while sport != 'Finish':
        result = input()

        if result == 'win':
            money += 20
            win_game += 1
        elif result == 'lose':
            loose_game += 1

        sport = input()
    if win_game > loose_game:
        money *= 1.1
        most_win += 1
    total_money += money


if most_win > day_count / 2:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
