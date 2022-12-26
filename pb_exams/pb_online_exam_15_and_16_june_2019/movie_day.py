pic_time = int(input())
scene_count = int(input())
scene_time = int(input())

preparation = pic_time * 0.15
recording_time = scene_count * scene_time
needed_time = preparation + recording_time
total_time = needed_time - pic_time
diff = abs(needed_time - pic_time)
if needed_time > pic_time:
    print(f"Time is up! To complete the movie you need {round(total_time)} minutes.")
else:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")

