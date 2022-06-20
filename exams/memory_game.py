# 100 / 100 Judge
elements = input().split()
comand = input()
moves = 1

# Add elements to middle in list of elements


def add_elements(index, elem):

    elements.insert(index, elem)


while comand != 'end':
    guess = comand.split()

    first_element = int(guess[0])
    second_element = int(guess[1])

    # Check for invalid input
    if first_element == second_element or first_element < 0 or second_element < 0 \
            or first_element >= len(elements) or second_element >= len(elements):

        element = '-' + str(moves) + 'a'
        ind = len(elements) // 2
        add_elements(ind, element)
        add_elements(ind, element)
        print("Invalid input! Adding additional elements to the board")
    # Check for two elements are match by index
    elif elements[first_element] == elements[second_element]:
        print(f"Congrats! You have found matching elements - {elements[first_element]}!")
        # Removing multiple elements from list by index
        delete_matched_elements = [first_element, second_element]
        for el in sorted(delete_matched_elements, reverse=True):
            del elements[el]
    else:
        print("Try again!")

    # Check does are no more elements left
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break

    moves += 1

    comand = input()

# Check does are left elements in sequence of elements
if len(elements) > 0:
    print('Sorry you lose :(')
    print(' '.join(elements))
