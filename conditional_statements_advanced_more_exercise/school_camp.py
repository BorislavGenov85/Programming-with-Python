season = input()
group = input()
students_count = int(input())
overnights_stays = int(input())

price = 0
sport = ""

if group == "boys":
    if season == "Winter":
        price = students_count * overnights_stays * 9.60
        sport = "Judo"
    elif season == "Spring":
        price = students_count * overnights_stays * 7.20
        sport = "Tennis"
    elif season == "Summer":
        price = students_count * overnights_stays * 15
        sport = "Football"

elif group == "girls":
    if season == "Winter":
        price = students_count * overnights_stays * 9.60
        sport = "Gymnastics"
    elif season == "Spring":
        price = students_count * overnights_stays * 7.20
        sport = "Athletics"
    elif season == "Summer":
        price = students_count * overnights_stays * 15
        sport = "Volleyball"

elif group == "mixed":
    if season == "Winter":
        price = students_count * overnights_stays * 10
        sport = "Ski"
    elif season == "Spring":
        price = students_count * overnights_stays * 9.50
        sport = "Cycling"
    elif season == "Summer":
        price = students_count * overnights_stays * 20
        sport = "Swimming"

if 10 <= students_count < 20:
    price *= 0.95
elif 20 <= students_count < 50:
    price *= 0.85
elif students_count >= 50:
    price *= 0.50

print(f"{sport} {price:.2f} lv.")
