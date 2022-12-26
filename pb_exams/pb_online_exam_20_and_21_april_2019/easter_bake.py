from math import ceil
from sys import maxsize

easter_bread_count = int(input())

total_sugar = 0
total_flour = 0
max_sugar = -maxsize
max_flour = -maxsize
needed_packets_sugar = 0
needed_packets_flour = 0
for i in range(1, easter_bread_count + 1):
    sugar_value_g = int(input())
    flour_value_g = int(input())

    if sugar_value_g > max_sugar:
        max_sugar = sugar_value_g

    if flour_value_g > max_flour:
        max_flour = flour_value_g

    total_sugar += sugar_value_g
    needed_packets_sugar = ceil(total_sugar / 950)
    total_flour += flour_value_g
    needed_packets_flour = ceil(total_flour / 750)

print(f"Sugar: {needed_packets_sugar}")
print(f"Flour: {needed_packets_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
