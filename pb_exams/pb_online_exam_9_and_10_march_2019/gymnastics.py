country = input()
appliance = input()

difficulty = 0
performance = 0
if country == "Russia":
    if appliance == "ribbon":
        difficulty += 9.100
        performance += 9.400
    elif appliance == "hoop":
        difficulty += 9.300
        performance += 9.800
    elif appliance == "rope":
        difficulty += 9.600
        performance += 9.000
elif country == "Bulgaria":

    if appliance == "ribbon":
         difficulty += 9.600
         performance += 9.400
    elif appliance == "hoop":
        difficulty += 9.550
        performance += 9.750
    elif appliance == "rope":
        difficulty += 9.500
        performance += 9.400
elif country == "Italy":
    if appliance == "ribbon":
        difficulty += 9.200
        performance += 9.500
    elif appliance == "hoop":
        difficulty += 9.450
        performance += 9.350
    elif appliance == "rope":
        difficulty += 9.700
        performance += 9.150

grade = difficulty + performance
diff = 20 - grade
percent_diff = diff / 20 * 100
print(f"The team of {country} get {grade:.3f} on {appliance}.")
print(f"{percent_diff:.2f}%")
