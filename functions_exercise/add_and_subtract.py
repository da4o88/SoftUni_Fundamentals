def sum_numbers(num1, num2):
    sum = num1 + num2
    return sum


def subtract(sum, num3):
    return sum - num3


first_number = int(input())
second_number = int(input())
third_number = int(input())

sum = sum_numbers(first_number, second_number)
result = subtract(sum, third_number)

print(result)
