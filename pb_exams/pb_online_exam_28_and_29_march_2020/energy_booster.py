# user input
fruit = input()
sett = input()
sett_count = int(input())
price = 0
# logic
if fruit == "Watermelon":
    if sett == "small":
        price += 2 * 56
    elif sett == "big":
        price += 5 * 28.70
elif fruit == "Mango":
    if sett == "small":
        price += 2 * 36.66
    elif sett == "big":
        price += 5 * 19.60
elif fruit == "Pineapple":
    if sett == "small":
        price += 2 * 42.10
    elif sett == "big":
        price += 5 * 24.80
elif fruit == "Raspberry":
    if sett == "small":
        price += 2 * 20
    elif sett == "big":
        price += 5 * 15.20

total_price = price * sett_count

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50
# output
print(f"{total_price:.2f} lv.")
