first_string = input()
second_string = input()

new_word = ""

for i in range(len(second_string)):
    if second_string[i] != first_string[i]:

        new_word += second_string[i]
        temp_word = first_string[(i + 1): len(second_string) + 1]

        print(new_word + temp_word)

    elif second_string[i] == first_string[i]:
        new_word += second_string[i]
