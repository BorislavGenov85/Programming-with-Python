year_tax = int(input())

shoes = year_tax * 0.60
team = shoes * 0.80
ball = team / 4
accessory = ball / 5

bill = year_tax + shoes + team + ball + accessory
print(f"{bill:.2f}")
