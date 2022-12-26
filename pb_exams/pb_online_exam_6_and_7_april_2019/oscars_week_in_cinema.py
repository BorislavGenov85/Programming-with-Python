film_name = input()
hall = input()
tickets = int(input())

price = 0
if film_name == "A Star Is Born":
    if hall == "normal":
        price = tickets * 7.50
    elif hall == "luxury":
        price = tickets * 10.50
    elif hall == "ultra luxury":
        price = tickets * 13.50
elif film_name == "Bohemian Rhapsody":
    if hall == "normal":
        price = tickets * 7.35
    elif hall == "luxury":
        price = tickets * 9.45
    elif hall == "ultra luxury":
        price = tickets * 12.75
elif film_name == "Green Book":
    if hall == "normal":
        price = tickets * 8.15
    elif hall == "luxury":
        price = tickets * 10.25
    elif hall == "ultra luxury":
        price = tickets * 13.25
elif film_name == "The Favourite":
    if hall == "normal":
        price = tickets * 8.75
    elif hall == "luxury":
        price = tickets * 11.55
    elif hall == "ultra luxury":
        price = tickets * 13.95

print(f"{film_name} -> {price:.2f} lv.")
