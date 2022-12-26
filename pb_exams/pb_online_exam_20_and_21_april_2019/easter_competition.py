easter_bread_count = int(input())
max_points = 0
baker_with_max_points = ""
for bread in range(easter_bread_count):
    baker_name = input()
    current_points = 0

    while True:
        grade = input()

        if grade == 'Stop':
            print(f"{baker_name} has {current_points} points.")
            break

        grade = int(grade)
        current_points += grade

    if current_points > max_points:
        max_points = current_points
        baker_with_max_points = baker_name
        print(f"{baker_name} is the new number 1!")

print(f"{baker_with_max_points} won competition with {max_points} points!")
