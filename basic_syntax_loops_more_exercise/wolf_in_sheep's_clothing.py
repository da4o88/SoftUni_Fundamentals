words = input()

list_words = words.split(',')

sheep_number = 0

if list_words[-1].strip() == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(list_words) - 1, -1, -1):
        if list_words[i].strip() == 'wolf':
            print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
            break
        else:
            sheep_number += 1

