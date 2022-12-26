budget = float(input())
actor_name = input()
fee_actor = 0

while actor_name != "ACTION":
    if len(actor_name) <= 15:
        fee_actor = float(input())
    else:
        fee_actor = budget * 0.20

    budget -= fee_actor

    if budget <= 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break

    actor_name = input()
if budget > 0:
    print(f"We are left with {budget:.2f} leva.")
