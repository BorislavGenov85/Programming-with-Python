number = int(input())

value = 0
diff = 0
current_value = 0
for i in range(1, number + 1):

    num_1 = int(input())
    num_2 = int(input())

    if i == 1:
        current_value += num_1 + num_2
        value = current_value
    elif i > 1:
        current_value += num_1 + num_2
        diff = current_value - value
max_diff = current_value - value
if value - diff == 0:
    print(f'Yes, value={value}')
else:
    print(f"No, maxdiff={max_diff}")
