words = input()

while words != "End":

    if words == "SoftUni":
        words = input()
        continue

    new_word = ''
    for i in words:
        new_word += (i * 2)

    print(new_word)
    words = input()



