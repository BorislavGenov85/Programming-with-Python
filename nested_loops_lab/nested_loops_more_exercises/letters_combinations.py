start = input()
end = input()
letter_3 = input()

combination = 0

for i in range(ord(start), ord(end) + 1):
    if i == ord(letter_3):
        continue
    for j in range(ord(start), ord(end) + 1):
        if j == ord(letter_3):
            continue
        for k in range(ord(start), ord(end) + 1):
            if k == ord(letter_3):
                continue
            combination += 1
            print(f"{chr(i)}{chr(j)}{chr(k)}", end=' ')

print(combination)
