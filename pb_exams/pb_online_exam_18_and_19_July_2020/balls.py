from math import floor
number = int(input())

total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_balls = 0
for i in range(1, number + 1):
    color = input()
    if color == "red":
        red_balls += 1
        total_points += 5
    elif color == "orange":
        orange_balls += 1
        total_points += 10
    elif color == "yellow":
        yellow_balls += 1
        total_points += 15
    elif color == "white":
        white_balls += 1
        total_points += 20
    elif color == "black":
        black_balls += 1
        total_points = floor(total_points / 2)
    else:
        other_balls += 1
        total_points = total_points

print(f"Total points: {total_points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")

