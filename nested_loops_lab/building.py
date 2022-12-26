floor_count = int(input())
rooms = int(input())
number = ""

for f in range(floor_count, 0, -1):
    for r in range(0, rooms):

        if f == floor_count:
            number = "L"
        elif f % 2 == 0:
            number = "O"
        else:
            number = "A"
        print(f"{number}{f}{r}", end=" ")
    print()
