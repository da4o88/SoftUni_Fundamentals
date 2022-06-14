def absolute_numbers(num):
    absolute_num = []
    for n in num:
        number = abs(n)
        absolute_num.append(number)
    return absolute_num


numbers = list(map(float, input().split(' ')))
abs_num = absolute_numbers(numbers)

print(abs_num)
