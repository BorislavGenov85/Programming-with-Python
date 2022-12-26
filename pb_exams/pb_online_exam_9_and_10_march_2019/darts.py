player_name = input()

total_points = 301
unsuccessful = 0
successful = 0

while True:
    field = input()
    if field == "Retire":
        print(f"{player_name} retired after {unsuccessful} unsuccessful shots.")
        break

    points = int(input())

    successful += 1

    if field == "Single":
        if total_points < points:
            unsuccessful += 1
            successful -= 1
            continue
        else:
            total_points -= points
    elif field == "Double":
        if total_points < points * 2:
            unsuccessful += 1
            successful -= 1
            continue
        else:
            total_points -= points * 2
    elif field == "Triple":
        if total_points < points * 3:
            unsuccessful += 1
            successful -= 1
            continue
        else:
            total_points -= points * 3

    if total_points == 0:
        print(f"{player_name} won the leg with {successful} shots.")
        break
