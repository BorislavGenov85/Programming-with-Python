height = int(input())
width = int(input())
no_painted_percent_area = int(input())
litters_paint = input()
kv_m = 0

total_area = height * width * 4
total_walls_for_paint = total_area - (total_area * no_painted_percent_area / 100)

while litters_paint != "Tired!":
    litters_paint = int(litters_paint)

    kv_m += litters_paint

    if total_walls_for_paint < kv_m:
        diff = abs(total_walls_for_paint - kv_m)
        print(f"All walls are painted and you have {diff:.0f} l paint left!")
        break

    if total_walls_for_paint - kv_m == 0:
        print("All walls are painted! Great job, Pesho!")
        break

    litters_paint = input()

if litters_paint == "Tired!":
    diff = abs(total_walls_for_paint - kv_m)
    print(f"{diff:.0f} quadratic m left.")

