budget = float(input())
nights_count = int(input())
price_on_night = float(input())
addition_tax_percents = int(input())
price_for_nights = nights_count * price_on_night

if nights_count > 7:
    price_for_nights *= 0.95
addition_tax = budget * addition_tax_percents / 100
needed_money = price_for_nights + addition_tax
diff = abs(budget - needed_money)
if budget >= needed_money:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
