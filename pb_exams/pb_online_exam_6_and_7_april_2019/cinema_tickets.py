movie_name = input()
all_ticket = 0
standard_tickets = 0
student_tickets = 0
kid_ticket = 0

flag = False
while movie_name != "Finish":
    current_movie = movie_name
    saloon_free_seats = int(input())

    ticket = input()
    sell_tickets = 0
    while ticket != "End":
        sell_tickets += 1
        all_ticket += 1
        if ticket == "student":
            student_tickets += 1
        elif ticket == "standard":
            standard_tickets += 1
        elif ticket == "kid":
            kid_ticket += 1

        if sell_tickets == saloon_free_seats or ticket == "End":
            break

        ticket = input()
    total_tickets = sell_tickets / saloon_free_seats * 100
    sell_tickets = 0
    print(f"{current_movie} - {total_tickets:.2f}% full.")

    movie_name = input()
    if movie_name == "Finish":
        flag = True
        break

percent_student_ticket = student_tickets / all_ticket * 100
percent_standard_ticket = standard_tickets / all_ticket * 100
percent_kid_ticket = kid_ticket / all_ticket * 100
if flag:
    print(f"Total tickets: {all_ticket}")
    print(f"{percent_student_ticket:.2f}% student tickets.")
    print(f"{percent_standard_ticket:.2f}% standard tickets.")
    print(f"{percent_kid_ticket:.2f}% kids tickets.")
