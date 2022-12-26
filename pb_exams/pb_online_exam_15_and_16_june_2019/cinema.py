hall_capacity = int(input())
people_count = input()
ticket = 5
price = 0
free_seats = hall_capacity
while people_count != "Movie time!":

    people_count = int(people_count)

    free_seats -= people_count
    if free_seats < 0:
        print("The cinema is full.")
        print(f"Cinema income - {price} lv.")
        break

    price += people_count * ticket
    if people_count % 3 == 0:
        price -= 5

    people_count = input()

diff = (hall_capacity - free_seats)
if people_count == "Movie time!" or free_seats == 0:
    print(f"There are {free_seats} seats left in the cinema.")
    print(f"Cinema income - {price} lv.")
