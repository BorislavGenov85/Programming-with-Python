size_of_eggs = input()
color_of_eggs = input()
lot_count = int(input())

price = 0
if size_of_eggs == "Large":
    if color_of_eggs == "Red":
        price = lot_count * 16
    elif color_of_eggs == "Green":
        price = lot_count * 12
    elif color_of_eggs == "Yellow":
        price = lot_count * 9
elif size_of_eggs == "Medium":
    if color_of_eggs == "Red":
        price = lot_count * 13
    elif color_of_eggs == "Green":
        price = lot_count * 9
    elif color_of_eggs == "Yellow":
        price = lot_count * 7
elif size_of_eggs == "Small":
    if color_of_eggs == "Red":
        price = lot_count * 9
    elif color_of_eggs == "Green":
        price = lot_count * 8
    elif color_of_eggs == "Yellow":
        price = lot_count * 5

expenses = price * 0.35
total_sum = price - expenses
print(f"{total_sum:.2f} leva.")

