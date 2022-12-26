name = input()
current_grade = float(input())

total_grades = 0
year_count = 0
felled_year = 0
while True:

    year_count += 1

    if current_grade >= 4:
        total_grades += current_grade
    elif current_grade < 4:
        felled_year += 1
        if felled_year > 1:
            print(f"{name} has been excluded at {year_count} grade")
            break
        year_count -= 1

    if year_count == 12:
        average_grade = total_grades / 12
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
    current_grade = float(input())
