budget = float(input())
year = int(input())
age = 18
money = 12000

for year in range(1800, year + 1):
    if age % 2 == 0:
        budget -= 12000
        year += 1
        age += 1
    else:
        budget -= 12000 + (age * 50)
        year += 1
        age += 1

total_budget = abs(budget)
if budget >= 0:
    print(f"Yes! He will live a carefree life and will have {budget:.2f} dollars left.")
else:
    print(f"He will need {total_budget:.2f} dollars to survive.")
