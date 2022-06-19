elements = input().split()
comand = input()
moves = 0

# Add elements to middle in list of elements


def add_elements(el):
    ind = len(elements) // 2
    elements.insert(ind, el)


while comand != 'end':
    guess = comand.split()
    # Check does are no more elements left
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break

    moves += 1

    # Check for invalid input
    if guess[0] == guess[1] or int(guess[0]) < 0 or int(guess[1]) < 0:
        element = '-' + str(moves) + 'a'
        add_elements(element)
        add_elements(element)
        print("Invalid input! Adding additional elements to the board")
    else:
        first_element = int(guess[0])
        second_element = int(guess[1])

        # Check for two elements are match by index
        if elements[first_element] == elements[second_element]:
            print(f"Congrats! You have found matching elements - {elements[first_element]}!")
            # Removing multiple elements from list by index
            delete_matched_elements = [first_element, second_element]
            for el in sorted(delete_matched_elements, reverse=True):
                del elements[el]

        else:
            print("Try again!")

    comand = input()

# Check does are left elements in sequence of elements
if len(elements) > 0:
    print('Sorry you lose :(')
    print(' '.join(elements))
