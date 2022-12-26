height = int(input())
width = int(input())
percent_of_area_not_painted = int(input())
litters_paint = input()
painted = 0

total_area = height * width * 4
walls_for_paint_kv_m = total_area - ((total_area * percent_of_area_not_painted) / 100)
diff = abs(walls_for_paint_kv_m - painted)
while True:
    if litters_paint == "Tired!":
        diff = abs(walls_for_paint_kv_m - painted)
        print(f"{diff:.0f} quadratic m left.")
        break
    litters_paint = int(litters_paint)
    painted += litters_paint

    if walls_for_paint_kv_m < painted:
        diff = abs(walls_for_paint_kv_m - painted)
        print(f"All walls are painted and you have {diff:.0f} l paint left!")
        break
    if walls_for_paint_kv_m - painted == 0:
        print("All walls are painted! Great job, Pesho!")
        break
    litters_paint = input()
