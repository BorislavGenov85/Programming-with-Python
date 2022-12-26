import sys

player_name = input()

max_score = -sys.maxsize
winner_name = ""

while player_name != "Stop":
    current_score = 0

    for letter in player_name:
        number = input()
        if int(number) == ord(letter):
            current_score += 10
        else:
            current_score += 2
        if current_score >= max_score:
            max_score = current_score
            winner_name = player_name
    player_name = input()

print(f'The winner is {winner_name} with {max_score} points!')
