guest_count = int(input())
an_envelop_for_one = float(input())
budget = float(input())

if 10 <= guest_count <= 15:
    an_envelop_for_one *= 0.85
elif 15 < guest_count <= 20:
    an_envelop_for_one *= 0.80
elif guest_count > 20:
    an_envelop_for_one *= 0.75

cake_price = budget * 0.10
total_sum = guest_count * an_envelop_for_one + cake_price
diff = abs(budget - total_sum)
if budget >= total_sum:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")
