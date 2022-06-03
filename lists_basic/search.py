n = int(input())
word_for_search = input()
list_of_words = []
filtered_list = []

for i in range(n):
    word = input()

    # Adding word to list of words
    list_of_words.append(word)

    # Check for word does exists in filtered list already.
    for words in list_of_words:
        if word_for_search in words:
            if words in filtered_list:
                continue
            else:
                filtered_list.append(words)


print(list_of_words)
print(filtered_list)
