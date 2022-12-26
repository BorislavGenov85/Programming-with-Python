baggage_price_over_twenty = float(input())
baggage_kg = float(input())
trip_days = int(input())
baggage_count = int(input())

baggage_tax = 0
if baggage_kg < 10:
    baggage_tax = baggage_price_over_twenty * 0.20
elif baggage_kg <= 20:
    baggage_tax = baggage_price_over_twenty * 0.50
elif baggage_kg > 20:
    baggage_tax = baggage_price_over_twenty

price_increase = 0
if trip_days < 7:
    price_increase = baggage_tax * 0.40
elif trip_days <= 30:
    price_increase = baggage_tax * 0.15
else:
    price_increase = baggage_tax * 0.10

total_baggage_price = baggage_tax + price_increase
total_sum = total_baggage_price * baggage_count
print(f" The total price of bags is: {total_sum:.2f} lv. ")
