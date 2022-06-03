n = int(input())
positive_list = []
negative_list = []

for i in range(n):
    number = int(input())

    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)

# Count negative sum and total positive number in list

sum_negative_numbers = 0
count_positive_numbers = len(positive_list)

for j in range(len(negative_list)):
    sum_negative_numbers += negative_list[j]

# Print results
print(positive_list)
print(negative_list)
print(f"Count of positives: {count_positive_numbers}\nSum of negatives: {sum_negative_numbers}")
