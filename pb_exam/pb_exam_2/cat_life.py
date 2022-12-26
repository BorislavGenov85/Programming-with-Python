breed = input()
sex = input()
if breed != "British Shorthair" and breed != "Siamese" and breed != "Persian" and breed != "Ragdoll" \
        and breed != "American Shorthair" and breed != "Siberian":
    print(f"{breed} is invalid cat!")
    exit()

in_human_mounts = 0
if breed == "British Shorthair":
    if sex == "m":
        in_human_mounts = 13 * 12
    elif sex == "f":
        in_human_mounts = 14 * 12
elif breed == "Siamese":
    if sex == "m":
        in_human_mounts = 15 * 12
    elif sex == "f":
        in_human_mounts = 16 * 12
elif breed == "Persian":
    if sex == "m":
        in_human_mounts = 14 * 12
    elif sex == "f":
        in_human_mounts = 15 * 12
elif breed == "Ragdoll":
    if sex == "m":
        in_human_mounts = 16 * 12
    elif sex == "f":
        in_human_mounts = 17 * 12
elif breed == "American Shorthair":
    if sex == "m":
        in_human_mounts = 12 * 12
    elif sex == "f":
        in_human_mounts = 13 * 12
elif breed == "Siberian":
    if sex == "m":
        in_human_mounts = 11 * 12
    elif sex == "f":
        in_human_mounts = 12 * 12

in_cat_mounts = round(in_human_mounts / 6)
print(f"{in_cat_mounts} cat months")


