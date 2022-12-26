group_count = int(input())
musala_count = 0
montblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
all_people = 0
for group in range(group_count):
    people = int(input())

    all_people += people

    if people <= 5:
        musala_count += people
    elif people <= 12:
        montblan_count += people
    elif people <= 25:
        kilimanjaro_count += people
    elif people <= 40:
        k2_count += people
    elif people > 40:
        everest_count += people

percent_musala = (musala_count / all_people) * 100
percent_montblan = (montblan_count / all_people) * 100
percent_kilimanjaro = (kilimanjaro_count / all_people) * 100
percent_k2 = (k2_count / all_people) * 100
percent_everest = (everest_count / all_people) * 100

print(f'{percent_musala:.2f}%')
print(f'{percent_montblan:.2f}%')
print(f'{percent_kilimanjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everest:.2f}%')
