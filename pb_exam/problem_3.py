day_count = int(input())
type_of_premises = input()
grade = input()

nights = day_count - 1
room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00
price = 0
if type_of_premises == 'room for one person':
    price += room_for_one_person * nights

elif type_of_premises == 'apartment':
    price += apartment * nights
    if day_count < 10:
        price *= 0.70
    elif 10 <= day_count <= 15:
        price *= 0.65
    elif day_count > 15:
        price *= 0.50

elif type_of_premises == 'president apartment':
    price += president_apartment * nights
    if day_count < 10:
        price *= 0.90
    elif 10 <= day_count <= 15:
        price *= 0.85
    elif day_count > 15:
        price *= 0.80

if grade == 'positive':
    price *= 1.25
elif grade == 'negative':
    price *= 0.90

print(f'{price:.2f}')
