visitors = int(input())
chest_count = 0
back_count = 0
legs_count = 0
abs_count = 0
shake_count = 0
bar_count = 0

for i in range(1, visitors + 1):
    activity = input()

    if activity == "Back":
        back_count += 1
    elif activity == "Chest":
        chest_count += 1
    elif activity == "Legs":
        legs_count += 1
    elif activity == "Abs":
        abs_count += 1
    elif activity == "Protein shake":
        shake_count += 1
    elif activity == "Protein bar":
        bar_count += 1

exercise_percent = ((back_count + chest_count + legs_count + abs_count) / visitors) * 100
protein_percent = ((shake_count + bar_count) / visitors) * 100
print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{shake_count} - protein shake")
print(f"{bar_count} - protein bar")
print(f"{exercise_percent:.2f}% - work out")
print(f"{protein_percent:.2f}% - protein")
