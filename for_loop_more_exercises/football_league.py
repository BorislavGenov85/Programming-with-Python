stadium_capacity = int(input())
all_fan = int(input())

sector_a_count = 0
sector_b_count = 0
sector_v_count = 0
sector_g_count = 0
for i in range(1, all_fan + 1):
    sector = input()

    if sector == "A":
        sector_a_count = sector_a_count + 1
    elif sector == "B":
        sector_b_count = sector_b_count + 1
    elif sector == "V":
        sector_v_count = sector_v_count + 1
    elif sector == "G":
        sector_g_count = sector_g_count + 1

percent_sector_a = (sector_a_count / all_fan) * 100
percent_sector_b = (sector_b_count / all_fan) * 100
percent_sector_v = (sector_v_count / all_fan) * 100
percent_sector_g = (sector_g_count / all_fan) * 100
percent_all_fan = (all_fan / stadium_capacity) * 100

print(f"{percent_sector_a:.2f}%")
print(f"{percent_sector_b:.2f}%")
print(f"{percent_sector_v:.2f}%")
print(f"{percent_sector_g:.2f}%")
print(f"{percent_all_fan:.2f}%")
