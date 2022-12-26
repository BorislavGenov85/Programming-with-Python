from math import floor
# user input
record_in_seconds = float(input())
distance_in_m = float(input())
time_in_sec_for_1m = float(input())

# logic
all_distance_in_sec = distance_in_m * time_in_sec_for_1m
delay = floor((distance_in_m / 50)) * 30
total_time = all_distance_in_sec + delay

# output
if total_time < record_in_seconds:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {abs(record_in_seconds - total_time):.2f} seconds slower.")
