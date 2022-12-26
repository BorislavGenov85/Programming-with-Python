from math import ceil

one_video_card_price = int(input())
one_transition_price = int(input())
current_electricity_for_day = float(input())
profit_for_one_card_per_day = float(input())

video_card = 13
transition = 13
other_components = 1000

price_for_cards = one_video_card_price * video_card
price_for_transitions = one_transition_price * transition
price_for_all = price_for_cards + price_for_transitions + other_components
price_per_card_for_day = profit_for_one_card_per_day - current_electricity_for_day
total_price_per_day_from_cards = video_card * price_per_card_for_day
day_for_return = ceil(price_for_all / total_price_per_day_from_cards)

print(price_for_all)
print(day_for_return)
