eggs_in_store = int(input())
command = input()
sell_eggs = 0
while command != "Close":

    buy_or_fill_eggs = int(input())
    if command == "Buy":
        if buy_or_fill_eggs > eggs_in_store:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_in_store}.")
            break
        sell_eggs += buy_or_fill_eggs
        eggs_in_store -= buy_or_fill_eggs
    elif command == "Fill":
        eggs_in_store += buy_or_fill_eggs

    command = input()

if command == "Close":
    print("Store is closed!")
    print(f"{sell_eggs} eggs sold.")
