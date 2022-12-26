word = input()
total_result = 0
m_p_w = ""
while word != "End of words":
    first_letter = word[0]
    current_result = 0
    result = 0
    for letter in word:
        current_char = ord(letter)
        current_result += current_char
        if first_letter[0] == "a" or first_letter[0] == "e" or first_letter[0] == "i" or first_letter[0] == "o" or \
                first_letter[0] == "u" or \
                first_letter[0] == "y" or first_letter[0] == "A" or first_letter[0] == "E" or first_letter[0] == "I" or \
                first_letter[0] == "O" or first_letter[0] == "U" or first_letter[0] == "Y":
            result = current_result * len(word)
        else:
            result = current_result / len(word)
    if result > total_result:
        total_result = result
        m_p_w = word

    word = input()

print(f"The most powerful word is {m_p_w} - {total_result}")
