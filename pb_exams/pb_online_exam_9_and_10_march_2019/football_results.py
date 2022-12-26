win_count = 0
loose_count = 0
draw_count = 0

first_match_result = input()
second_match_result = input()
third_match_result = input()
if ord(first_match_result[0]) > ord(first_match_result[2]):
    win_count += 1
elif ord(first_match_result[0]) < ord(first_match_result[2]):
    loose_count += 1
else:
    draw_count += 1

if ord(second_match_result[0]) > ord(second_match_result[2]):
    win_count += 1
elif ord(second_match_result[0]) < ord(second_match_result[2]):
    loose_count += 1
else:
    draw_count += 1

if ord(third_match_result[0]) > ord(third_match_result[2]):
    win_count += 1
elif ord(third_match_result[0]) < ord(third_match_result[2]):
    loose_count += 1
else:
    draw_count += 1

print(f"Team won {win_count} games.")
print(f"Team lost {loose_count} games.")
print(f" Drawn games: {draw_count}")
