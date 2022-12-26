coins_count_1 = int(input())
coins_count_2 = int(input())
banknotes_count_5 = int(input())
total = int(input())
sum1 = 0
sum2 = 0
sum3 = 0
for i in range(coins_count_1 + 1):
    for j in range(coins_count_2 + 1):
        for k in range(banknotes_count_5 + 1):
            sum1 = i * 1
            sum2 = j * 2
            sum3 = k * 5
            total_sum = sum1 + sum2 + sum3
            if sum1 + sum2 + sum3 == total:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {total} lv.")
