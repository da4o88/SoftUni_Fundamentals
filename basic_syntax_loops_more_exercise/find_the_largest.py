number = int(input())
largest_number = []

number = str(number)

for i in range(len(number)):
    largest_number.append(number[i])

largest_number.sort(reverse=True)

print("".join(largest_number))



