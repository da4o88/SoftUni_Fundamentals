number = int(input())


def tribonaccie_numbers(num):
    numbers = []
    # sum_numbers = 0

    for i in range(num):
        if i < 2:
            sum_numbers = 1
            numbers.append(sum_numbers)
        elif i < 3:
            sum_numbers = 2
            numbers.append(sum_numbers)
        else:
            sum_numbers = numbers[-1] + numbers[-2] + numbers[-3]
            numbers.append(sum_numbers)

    return numbers


result = tribonaccie_numbers(number)
result = [str(s) for s in result]

print(' '.join(result))
