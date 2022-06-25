number_1 = int(input())
number_2 = int(input())
number_3 = int(input())


def multiplication_result(num1, num2, num3):
    numbers = [num1, num2, num3]
    neg_count = 0
    result = ''
    for n in numbers:
        if n == 0:
            return 'zero'
        elif n < 0:
            neg_count += 1
        else:
            result = 'positive'

    if neg_count > 0 and neg_count != 2:
        result = 'negative'

    return result


res = multiplication_result(number_1, number_2, number_3)
print(res)
