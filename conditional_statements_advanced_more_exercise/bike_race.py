junior_cyclist_count = int(input())
senior_cyclist_count = int(input())
route = input()

tax = 0
junior_tax = 0
senior_tax = 0

if route == "trail":
    junior_tax = junior_cyclist_count * 5.50
    senior_tax = senior_cyclist_count * 7
    tax = junior_tax + senior_tax

elif route == "cross-country":
    junior_tax = junior_cyclist_count * 8
    senior_tax = senior_cyclist_count * 9.50
    tax = junior_tax + senior_tax
    if junior_cyclist_count + senior_cyclist_count >= 50 and route == "cross-country":
        tax *= 0.75

elif route == "downhill":
    junior_tax = junior_cyclist_count * 12.25
    senior_tax = senior_cyclist_count * 13.75
    tax = junior_tax + senior_tax

elif route == "road":
    junior_tax = junior_cyclist_count * 20
    senior_tax = senior_cyclist_count * 21.50
    tax = junior_tax + senior_tax

expenses = tax * 0.05
donated_sum = tax - expenses
print(f"{donated_sum:.2f}")
