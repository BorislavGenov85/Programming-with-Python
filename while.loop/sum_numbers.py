number = int(input())

sum_number = 0
while sum_number <= number:
    current_num = int(input())
    sum_number += current_num

    if sum_number >= number:
        print(sum_number)
        break
