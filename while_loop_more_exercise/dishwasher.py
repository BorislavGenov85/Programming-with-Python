detergent = int(input()) * 750
preparation = 0
dishes = 0
pots_count = 0
plates_count = 0
used_detergent = 0
while used_detergent >= 0:
    user_input = input()
    dishes += 1

    if user_input == "End":
        break
    user_input = int(user_input)

    if dishes % 3 == 0:
        preparation += user_input * 15
        used_detergent = detergent - preparation
        pots_count += user_input
    else:
        preparation += user_input * 5
        used_detergent = detergent - preparation
        plates_count += user_input

diff = abs(detergent - preparation)
if used_detergent >= 0:
    print("Detergent was enough!")
    print(f"{plates_count} dishes and {pots_count} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")
