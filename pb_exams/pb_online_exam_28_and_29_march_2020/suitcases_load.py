cargo_capacity = float(input())
suitcase_volume = input()
curr_capacity = cargo_capacity
iteration = 0
success_case = 0

check = False
while suitcase_volume != "End":
    curr_volume = float(suitcase_volume)
    iteration += 1
    if iteration == 3:
        curr_volume = curr_volume * 110 / 100
    if curr_volume >= curr_capacity:
        check = True
        break
    curr_capacity -= curr_volume
    success_case += 1
    suitcase_volume = input()

if check:
    print("No more space!")
    print(f"Statistic: {success_case} suitcases loaded.")
else:
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {success_case} suitcases loaded.")
