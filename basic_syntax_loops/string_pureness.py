n = int(input())

for i in range(n):
    word = input()

    if ',' not in word and '.' not in word and '_' not in word:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")
