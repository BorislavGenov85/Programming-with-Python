from sys import maxsize

player_name = input()
max_goals = -maxsize
best_player = ""
flag = False
while player_name != "END":
    goals = int(input())

    if goals > max_goals:
        max_goals = goals
        best_player = player_name

    if goals >= 10:
        flag = True
        break

    if goals >= 3:
        flag = True

    player_name = input()

print(f"{best_player} is the best player!")
if flag:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
