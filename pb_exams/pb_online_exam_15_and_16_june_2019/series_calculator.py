from math import floor
serial_name = input()
seasons_count = int(input())
episode_count = int(input())
episode_time = float(input())

advertisement = episode_time * 0.20
episode_time_with_adv = episode_time + advertisement
extra_time = seasons_count * 10
total_time = episode_time_with_adv * episode_count * seasons_count + extra_time

print(f"Total time needed to watch the {serial_name} series is {floor(total_time)} minutes.")
