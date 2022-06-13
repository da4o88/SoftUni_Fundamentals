number_of_char = list(map(int, input().split(' ')))
entry_message = list(input())

message = []

i = len(entry_message)


for i in range(len(number_of_char)):
    # Sum of digits from number in list
    sum = 0
    for digit in str(number_of_char[i]):
        sum += int(digit)
    # Find index of char in list and add to new list a remove from string
    if len(entry_message) > sum:
        message.append(entry_message[sum])
        entry_message.pop(sum)
    else:
        while sum > len(entry_message):
            sum -= len(entry_message)

        message.append(entry_message[sum])
        entry_message.pop(sum)

print(''.join(message))
