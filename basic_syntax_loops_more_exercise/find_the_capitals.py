word = input()
capital_leters_pos = []

for i in range(len(word)):
    if word[i].isupper():
        capital_leters_pos.append(i)

print(capital_leters_pos)

