day_count = int(input())
hour_count = int(input())
total = 0
for i in range(1, day_count + 1):
    price = 0
    for j in range(1, hour_count + 1):
        if i % 2 == 0 and j % 2 != 0:
            total += 2.50
            price += 2.50
        elif i % 2 != 0 and j % 2 == 0:
            total += 1.25
            price += 1.25
        else:
            total += 1
            price += 1
    print(f"Day: {i} - {price:.2f} leva")
print(f"Total: {total:.2f} leva")

