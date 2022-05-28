words = input()

words = words.upper()
counter = 0

chosen_words = ['Sand', 'Water', 'Fish', 'Sun']

for i in range(len(chosen_words)):
    chosen_word = chosen_words[i].upper()
    count = words.count(chosen_word)
    counter += count

print(counter)
