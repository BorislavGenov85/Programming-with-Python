from sys import maxsize

painted_egg_count = int(input())

max_num = -maxsize
red_count = 0
orange_count = 0
blue_count = 0
green_count = 0
color = ""
max_egg = 0
for egg in range(painted_egg_count):
    color_of_agg = input()

    if color_of_agg == "red":
        red_count += 1
    elif color_of_agg == "orange":
        orange_count += 1
    elif color_of_agg == "blue":
        blue_count += 1
    elif color_of_agg == "green":
        green_count += 1

    if red_count > orange_count and red_count > blue_count and red_count > green_count:
        color = "red"
        max_egg = red_count
    elif orange_count > red_count and orange_count > blue_count and orange_count > green_count:
        color = "orange"
        max_egg = orange_count
    elif blue_count > red_count and blue_count > orange_count and blue_count > green_count:
        color = "blue"
        max_egg = blue_count
    elif green_count > red_count and green_count > orange_count and green_count > blue_count:
        color = "green"
        max_egg = green_count

print(f"Red eggs: {red_count}")
print(f"Orange eggs: {orange_count}")
print(f"Blue eggs: {blue_count}")
print(f"Green eggs: {green_count}")
print(f"Max eggs: {max_egg} -> {color}")
