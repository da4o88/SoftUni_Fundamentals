number = int(input())


def perfect_number(num):

    sum = sum_of_divisors(num)

    if num == sum:
        return True
    else:
        return False


def sum_of_divisors(number):

    divisors = []
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            divisors.append(i)

    sum_divisors = sum(divisors)

    return sum_divisors


if number > 1:
    number_is_perfect = perfect_number(number)
    if number_is_perfect:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
