needed_money = float(input())
init_money = float(input())

total_money = init_money
days_count = 0
spend_days_count = 0
flag = False
while total_money < needed_money:
    action = input()
    money = float(input())

    days_count += 1

    if action == "spend":
        spend_days_count += 1
        total_money -= money
        if total_money < money:
            total_money = 0
    elif action == "save":
        total_money += money
        spend_days_count = 0

    if spend_days_count == 5:
        flag = True
        break

if flag:
    print("You can't save the money.")
    print(f"{days_count}")
else:
    print(f"You saved the money for {days_count} days.")
