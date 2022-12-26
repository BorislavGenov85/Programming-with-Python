destination = input()
total_sum = 0
while destination != "End":

    min_budget = float(input())
    while total_sum <= min_budget:
        current_sum = float(input())
        total_sum += current_sum

        if total_sum >= min_budget:
            print(f"Going to {destination}!")
            total_sum = 0
            break
    destination = input()
    if destination == "End":
        break

