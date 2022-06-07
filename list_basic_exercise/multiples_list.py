factor = int(input())
count = int(input())

multiple_factor_list = []
n = 1


while len(multiple_factor_list) < count:
    if factor > 0:
        if n % factor == 0:
            multiple_factor_list.append(n)
        n += 1
print(multiple_factor_list)
