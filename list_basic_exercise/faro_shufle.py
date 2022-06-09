cards = list(input().split(' '))
number_of_shuffling = int(input())

# Check does number for shuffling cards is positive number and not 0
if number_of_shuffling == 0 or number_of_shuffling < 0:
    print("Your number of shuffling is incorect!")

# Shuffle the cards once
first_half = cards[:len(cards) // 2]
second_half = cards[len(cards) // 2:]

shuffled_cards = [desk for pair in zip(first_half, second_half) for desk in pair]

# If number of shuffling is more than once
if number_of_shuffling > 1:
    for i in range(1, number_of_shuffling):
        first_half = shuffled_cards[:len(shuffled_cards) // 2]
        second_half = shuffled_cards[len(shuffled_cards) // 2:]

        shuffled_cards = [desk for pair in zip(first_half, second_half) for desk in pair]

print(shuffled_cards)
