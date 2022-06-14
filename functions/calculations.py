
def calc(op, num1, num2):
    result = 0
    if op == 'multiply':
        result = num1 * num2
    elif op == 'divide':
        result = num1 / num2
    elif op == 'subtract':
        result = num1 - num2
    elif op == 'add':
        result = num1 + num2

    return int(result)


operator = input()
first_number = int(input())
second_number = int(input())

res = calc(operator, first_number, second_number)
print(res)
