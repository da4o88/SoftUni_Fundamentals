def char_in_range(ch1, ch2):
    all_characters = []

    for ch in range(ord(ch1) + 1, ord(ch2)):
        all_characters.append(chr(ch))

    return all_characters


first_character = input()
second_character = input()
result = char_in_range(first_character, second_character)

print(' '.join(result))
