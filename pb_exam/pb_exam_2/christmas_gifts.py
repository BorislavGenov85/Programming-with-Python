input_line = input()
adults_count = 0
kids_count = 0
price_for_toy = 5
price_for_sweater = 15
toy_count = 0
while input_line != 'Christmas':

    age = int(input_line)
    if age <= 16:
        kids_count += 1
    elif age > 16:
        adults_count += 1

    input_line = input()

money_for_toys = kids_count * price_for_toy
money_for_sweaters = adults_count * price_for_sweater
print(f"Number of adults: {adults_count}")
print(f"Number of kids: {kids_count}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")
