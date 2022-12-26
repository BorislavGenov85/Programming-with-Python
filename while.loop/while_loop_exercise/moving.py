weight = int(input())
length = int(input())
height = int(input())
space = weight * length * height
free_space = 0
boxes = input()

while boxes != "Done":
    boxes = int(boxes)

    free_space += boxes
    if free_space >= space:
        break

    boxes = input()

diff = abs(space - free_space)

if boxes == "Done":
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")
