from math import floor

tournament_count = int(input())
points = int(input())

w_count = 0
total_points = points
for i in range(1, tournament_count + 1):
    stage = input()
    if stage == "W":
        total_points += 2000
        w_count += 1
    elif stage == "F":
        total_points += 1200
    elif stage == "SF":
        total_points += 720

average_points = (total_points - points) / tournament_count
w_percent = (w_count / tournament_count) * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{w_percent:.2f}%")
