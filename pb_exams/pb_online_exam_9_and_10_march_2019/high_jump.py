max_height = int(input())

current_height = max_height - 30
limit = 0
count_jumps = 0
count_bad_try = 0
max_jump = 0

while True:
    for height in range(2):
        jump = int(input())
        count_jumps += 1

        if jump <= current_height:
            count_bad_try += 1
            if count_bad_try == 3:
                print(f'Tihomir failed at {current_height}cm after {count_jumps} jumps.')
                break

        if jump > current_height:
            count_bad_try = 0
            if current_height >= max_height:
                limit = current_height
                print(f'Tihomir succeeded, he jumped over {current_height}cm after {count_jumps} jumps.')
                break
            current_height += 5
            break

    if count_bad_try == 3:
        break
    if limit >= max_height:
        break
