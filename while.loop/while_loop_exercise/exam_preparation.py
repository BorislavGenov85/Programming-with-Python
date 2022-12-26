poor_grade_count = int(input())
task_name = input()

flag = False
poor_grade = 0
total_grade = 0
task_solve = 0
last_task = ""
while task_name != "Enough":
    grade = int(input())
    task_solve += 1

    if grade <= 4:
        poor_grade += 1
        total_grade += grade
    else:
        total_grade += grade

    if poor_grade == poor_grade_count:
        flag = True
        break

    last_task = task_name
    task_name = input()


average_grade = total_grade / task_solve
if flag:
    print(f"You need a break, {poor_grade} poor grades.")
else:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {task_solve}")
    print(f"Last problem: {last_task}")
