numbers = list(map(int, input().split(', ')))
final_numbers = []
zero_list = []

for num in numbers:
    if num != 0:
        final_numbers.append(num)
    else:
        zero_list.append(num)

final_numbers.extend(zero_list)
print(final_numbers)
