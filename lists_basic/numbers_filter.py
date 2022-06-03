n = int(input())
numbers = []
filtered_numbers = []
# Add all numbers in empty list
for i in range(n):
    number = int(input())
    numbers.append(number)

command = input()

# Check the command input for all numbers in list
for j in numbers:
    if command == 'even':
        if j == 0:
            filtered_numbers.append(j)
            continue
        if j % 2 == 0:
            filtered_numbers.append(j)

    elif command == 'odd':
        if not (j % 2 == 0):
            filtered_numbers.append(j)
    elif command == 'positive':
        if j >= 0:
            filtered_numbers.append(j)

    elif command == 'negative':
        if j < 0:
            filtered_numbers.append(j)

# Print the created list with the given command ('even', 'odd', 'positive', 'negative')
print(filtered_numbers)
