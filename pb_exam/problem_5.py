input_line = input()
number = int(input())
base_camp = 5364
top = 8848
day = 1
flag = False
while input_line != 'END':
    if input_line == 'Yes':
        day += 1
    else:
        pass

    overnight_stay = input_line
    current_m = number

    base_camp += current_m

    if base_camp > top:
        flag = True
        break

    if day == 5:
        break
    input_line = input()
    if input_line == 'END':
        break
    number = int(input())
if flag:
    print(f"Goal reached for {day} days!")
else:
    print("Failed!")
    print(f"{base_camp}")
