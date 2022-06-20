
def round_numbers(nums):
    rounded_numbers = []
    for num in nums:
        n = round(num)
        rounded_numbers.append(n)

    return rounded_numbers


numbers = list(map(float,input().split(' ')))

result = round_numbers(numbers)

print(result)
