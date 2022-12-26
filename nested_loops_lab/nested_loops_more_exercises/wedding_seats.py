last_sector = input()
row_count_in_sector_1 = int(input())
seats_count_even_row = int(input())

first_sector = 65
first_seat = 97
count = 0

for i in range(first_sector, ord(last_sector) + 1):
    for j in range(1, row_count_in_sector_1 + 1):
        if j % 2 != 0:
            for k in range(first_seat, (first_seat + seats_count_even_row)):
                count += 1
                print(f"{chr(i)}{j}{chr(k)}")

        elif j % 2 == 0:
            for k in range(first_seat, (first_seat + seats_count_even_row + 2)):
                count += 1
                print(f"{chr(i)}{j}{chr(k)}")
    if row_count_in_sector_1 + 1 > row_count_in_sector_1:
        row_count_in_sector_1 += 1
print(count)
