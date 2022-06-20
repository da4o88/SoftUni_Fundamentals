# Even numbers with filter()
numbers = list(map(int, input().split(' ')))


def even_numbers(number):
    return number % 2 == 0


result = filter(even_numbers, numbers)

print(list(result))
