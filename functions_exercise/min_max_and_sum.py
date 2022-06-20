numbers = list(map(int, input().split(' ')))

def min_number(numbers):
    return min(numbers)


def max_number(numbers):
    return max(numbers)


def sum_of_numbers(numbers):
    return sum(numbers)


minimum_number = min_number(numbers)
maximum_number = max_number(numbers)
sum_numbers = sum_of_numbers(numbers)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_numbers}")
