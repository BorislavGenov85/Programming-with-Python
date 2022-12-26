group = int(input())
musala_count = 0
montblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
for i in range(1, group + 1):
    people_count = int(input())

    if people_count <= 5:
        musala_count = musala_count + people_count
    elif people_count <= 12:
        montblan_count = montblan_count + people_count
    elif people_count <= 25:
        kilimanjaro_count = kilimanjaro_count + people_count
    elif people_count <= 40:
        k2_count = k2_count + people_count
    elif people_count > 40:
        everest_count = everest_count + people_count

total_people = musala_count + montblan_count + kilimanjaro_count + k2_count + everest_count
percent_musala = musala_count / total_people * 100
percent_montblan = montblan_count / total_people * 100
percent_kilimanjaro = kilimanjaro_count / total_people * 100
percent_k2 = k2_count / total_people * 100
percent_everest = everest_count / total_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_montblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
