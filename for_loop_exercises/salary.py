browser_count = int(input())
total_salary = float(input())

salary = total_salary
for i in range(1, browser_count + 1):
    web_name = input()
    if salary <= 0:
        break

    if web_name == "Facebook":
        salary = salary - 150
    elif web_name == "Instagram":
        salary = salary - 100
    elif web_name == "Reddit":
        salary = salary - 50

if salary <= 0:
    print(f"You have lost your salary.")
else:
    print(f"{salary:.0f}")
