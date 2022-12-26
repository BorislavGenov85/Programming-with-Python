book = input()
checked_book = 0
is_found = False
current_book = input()
while current_book != "No More Books":
    if current_book == book:
        is_found = True
        break

    checked_book += 1

    current_book = input()

if is_found:
    print(f"You checked {checked_book} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {checked_book} books.")
