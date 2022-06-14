
def sum_odd_num(number):
    num = [int(n) for n in str(number)]
    sum = 0

    for i in num:
        if i % 2 != 0:
            sum += i
    return sum


def sum_even_num(number):
    num = [int(n) for n in str(number)]
    sum = 0

    for i in num:
        if i % 2 == 0:
            sum += i
    return sum

number = int(input())

sum_even_digits = sum_even_num(number)
sum_odd_digits = sum_odd_num(number)

print(f"Odd sum = {sum_odd_digits}, Even sum = {sum_even_digits}")
