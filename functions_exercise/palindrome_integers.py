numbers = list(map(int, input().split(', ')))


def is_palindrome(num):
    number = str(num)
    # Check string is equal to reverse string
    if (number == number[::-1]):
        return True
    else:
        return False


for number in numbers:

    result = is_palindrome(number)
    print(result)
