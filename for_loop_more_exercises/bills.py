months = int(input())
water = 20
internet = 15
other = 0
sum_for_other = 0
total_electricity = 0
for i in range(1, months + 1):
    bill_for_electricity = float(input())

    total_electricity = total_electricity + bill_for_electricity
    other = (bill_for_electricity + water + internet) * 1.2
    sum_for_other += other

total_water = water * months
total_internet = internet * months
total_bill = (total_electricity + total_water + total_internet + sum_for_other) / months
print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {sum_for_other:.2f} lv")
print(f"Average: {total_bill:.2f} lv")
