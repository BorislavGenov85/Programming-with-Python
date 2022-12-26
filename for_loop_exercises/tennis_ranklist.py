from math import floor
tournament_number = int(input())
started_points = int(input())

final_points = started_points
w_points = 0
f_points = 0
sf_points = 0
w_count = 0
for i in range(1, tournament_number + 1):
    final = input()

    if final == "W":
        final_points = final_points + 2000
        w_points = w_points + 2000
        w_count = w_count + 1
    elif final == "F":
        final_points = final_points + 1200
        f_points = f_points + 1200
    elif final == "SF":
        final_points = final_points + 720
        sf_points = sf_points + 720

middle_points = (w_points + f_points + sf_points) / tournament_number
percent_w_t = w_count / tournament_number * 100
print(f"Final points: {final_points}")
print(f"Average points: {floor(middle_points)}")
print(f"{percent_w_t:.2f}%")
