tournament_name = input()
win_mach = 0
loose_mach = 0
total_mach = 0
while tournament_name != "End of tournaments":

    mach_count = int(input())
    total_mach += mach_count
    for current_mach in range(1, mach_count + 1):
        desi_team_points = int(input())
        opponent_team_points = int(input())

        if desi_team_points > opponent_team_points:
            diff = abs(desi_team_points - opponent_team_points)
            win_mach += 1
            print(f"Game {current_mach} of tournament {tournament_name}: win with {diff} points.")

        elif desi_team_points < opponent_team_points:
            diff = abs(desi_team_points - opponent_team_points)
            loose_mach += 1
            print(f"Game {current_mach} of tournament {tournament_name}: lost with {diff} points.")

    tournament_name = input()

percent_win_mach = win_mach / total_mach * 100
percent_loose_mach = loose_mach / total_mach * 100
if tournament_name == "End of tournaments":
    print(f"{percent_win_mach:.2f}% matches win")
    print(f"{percent_loose_mach:.2f}% matches lost")
