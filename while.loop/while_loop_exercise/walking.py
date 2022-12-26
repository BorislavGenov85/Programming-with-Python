action = input()
total_steps = 0

while action != "Going home":
    action = int(action)

    total_steps += action
    if total_steps > 10000:
        break

    action = input()
if action == "Going home":
    step_home = int(input())
    total_steps += step_home

diff = abs(10000 - total_steps)

if total_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")


