needed_sum = int(input())
input_line = input()

cash = 0
cash_count = 0
card = 0
card_count = 0
counter = 0
flag = False
while input_line != 'End':
    current_price = int(input_line)
    counter += 1
    if counter % 2 != 0:
        if current_price > 100:
            print("Error in transaction!")
        elif current_price <= 100:
            cash += current_price
            cash_count += 1
            print("Product sold!")
    elif counter % 2 == 0:
        if current_price < 10:
            print("Error in transaction!")
        elif current_price >= 10:
            card += current_price
            card_count += 1
            print("Product sold!")

    if (card + cash) >= needed_sum:
        flag = True
        break
    input_line = input()

average_cash = cash / cash_count
average_card = card / card_count
if flag:
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")
else:
    print("Failed to collect required money for charity.")
