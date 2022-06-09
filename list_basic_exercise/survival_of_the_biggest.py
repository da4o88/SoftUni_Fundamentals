from sys import maxsize

numbers = list(map(int, input().split(' ')))
removals = int(input())

for _ in range(removals):
    min_number = maxsize

    for i in range(len(numbers)):
        if numbers[i] < min_number:
            min_number = numbers[i]

    numbers.remove(min_number)

print(', '.join(str(num) for num in numbers))

