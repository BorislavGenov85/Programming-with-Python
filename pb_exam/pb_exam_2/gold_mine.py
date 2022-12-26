location_count = int(input())

for i in range(location_count):
    expected_mining = float(input())
    day_count = int(input())

    current_gold = 0
    for j in range(day_count):
        gold = float(input())
        current_gold += gold

    average_mining = current_gold / day_count
    diff = expected_mining - average_mining
    if expected_mining <= average_mining:
        print(f"Good job! Average gold per day: {average_mining:.2f}.")
    elif expected_mining > average_mining:
        print(f"You need {diff:.2f} gold.")
