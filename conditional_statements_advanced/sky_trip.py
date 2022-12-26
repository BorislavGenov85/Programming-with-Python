day_count = int(input())
room = input()
grade = input()
price = 0
if room == "room for one person":
    price = (day_count - 1) * 18
elif room == "apartment":
    price = (day_count - 1) * 25
    if day_count < 10:
        price *= 0.70
    elif day_count < 15:
        price *= 0.65
    elif day_count > 15:
        price *= 0.50
elif room == "president apartment":
    price = (day_count - 1) * 35
    if day_count < 10:
        price *= 0.90
    elif day_count < 15:
        price *= 0.85
    elif day_count > 15:
        price *= 0.80

if grade == "positive":
    price *= 1.25
elif grade == "negative":
    price *= 0.90

print(f"{price:.2f}")
