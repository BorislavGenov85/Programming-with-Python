people_juri = int(input())
presentation = input()
avg_grade_all = 0
grade_count = 0
while presentation != "Finish":
    pres_grade = 0
    for grade in range(1, people_juri + 1):
        current_grade = float(input())

        grade_count += 1
        pres_grade += current_grade
        avg_grade_all += current_grade

    avg_grade = pres_grade / people_juri
    print(f"{presentation} - {avg_grade:.2f}.")

    presentation = input()

final_assessment = avg_grade_all / grade_count
print(f"Student's final assessment is {final_assessment:.2f}.")
