actor_name = input()
first_points = float(input())
evaluative_count = int(input())

points_count = first_points
for i in range(1, evaluative_count + 1):
    ev_name = input()
    ev_points = float(input())

    points_count += (len(ev_name) * ev_points) / 2

    if points_count >= 1250.5:
        break

if points_count >= 1250:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points_count:.1f}!")
else:
    needed_points = 1250.5 - points_count
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
