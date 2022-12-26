students_count = int(input())

total_weak_count = 0
total_weak_minded_count = 0
total_good_count = 0
total_very_good_count = 0
final_grade = 0
for i in range(1, students_count + 1):
    grade_from_exam = float(input())

    weak_count = 0
    weak_minded_count = 0
    good_count = 0
    very_good_count = 0
    total_grade = grade_from_exam
    if 2.00 <= grade_from_exam <= 2.99:
        weak_count += 1
    elif grade_from_exam <= 3.99:
        weak_minded_count += 1
    elif grade_from_exam <= 4.99:
        good_count += 1
    elif grade_from_exam >= 5:
        very_good_count += 1

    final_grade += total_grade
    total_weak_count += weak_count
    total_weak_minded_count += weak_minded_count
    total_good_count += good_count
    total_very_good_count += very_good_count
percent_weak = (total_weak_count / students_count) * 100
percent_minded = (total_weak_minded_count / students_count) * 100
percent_good = (total_good_count / students_count) * 100
percent_very_good = (total_very_good_count / students_count) * 100
average = final_grade / students_count

print(f"Top students: {percent_very_good:.2f}%")
print(f"Between 4.00 and 4.99: {percent_good:.2f}%")
print(f"Between 3.00 and 3.99: {percent_minded:.2f}%")
print(f"Fail: {percent_weak:.2f}%")
print(f"Average: {average:.2f}")

