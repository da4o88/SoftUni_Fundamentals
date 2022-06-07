items = input()
number_of_beggars = int(input())

items = items.split(', ')
list_items = []
list_of_beggars = []
# Create new list with converted string to integer from items
for i in items:
    list_items.append(int(i))

sum_of_beggars = []

# Create nested list for every item that beggars take back
count = 0
while count < number_of_beggars:
    temp_list = []
    for j in range(count, len(list_items), number_of_beggars):
        temp_list.append(list_items[j])

    list_of_beggars.append(temp_list)
    count += 1

# Sum of items for each beggar
sum_of_items = 0
for list_of_items in list_of_beggars:
    for element in list_of_items:
        sum_of_items += element
    sum_of_beggars.append(sum_of_items)
    sum_of_items = 0

print(sum_of_beggars)
