actor_name = input()
current_points = float(input())
evaluative_count = int(input())

point_counter = current_points
for i in range(1, evaluative_count + 1):
    name = input()
    points = float(input())

    point_counter += (len(name) * points) / 2

    if point_counter >= 1250.5:
        break

if point_counter >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {point_counter:.1f}!")
else:
    needed_points = 1250.5 - point_counter
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
