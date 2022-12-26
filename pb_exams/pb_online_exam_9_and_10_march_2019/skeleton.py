control_in_minutes = int(input())
control_in_seconds = int(input())
length_in_m = float(input())
seconds_for_100_m = int(input())

control_time = (control_in_minutes * 60) + control_in_seconds
delay = length_in_m / 120
total_delay = delay * 2.5
his_time = (length_in_m / 100) * seconds_for_100_m - total_delay
needed_seconds = abs(control_time - his_time)
if his_time <= control_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {his_time:.3f}.")
else:
    print(f"No, Marin failed! He was {needed_seconds:.3f} second slower.")
