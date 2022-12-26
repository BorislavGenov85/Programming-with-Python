computers_count = int(input())
current_sell = 0
current_rating = 0
for i in range(computers_count):
    number = int(input())

    reiting = number % 10
    sell = number // 10

    if reiting == 2:
        current_rating += reiting
        current_sell += 0
    elif reiting == 3:
        current_sell += sell * 0.50
        current_rating += reiting
    elif reiting == 4:
        current_sell += sell * 0.70
        current_rating += reiting
    elif reiting == 5:
        current_sell += sell * 0.85
        current_rating += reiting
    elif reiting == 6:
        current_sell += sell
        current_rating += reiting
avr_rating = current_rating / computers_count
print(f"{current_sell:.2f}")
print(f"{avr_rating:.2f}")

