number = int(input())
special_number = False

for i in range(1, number + 1):
    sum = 0
    num = str(i)

    for j in range(len(num)):
        sum += int(num[j])

    if sum == 5 or sum == 7 or sum == 11:
        special_number = True
    else:
        special_number = False

    if special_number:
        print(f"{i} -> {special_number}")
    else:
        print(f"{i} -> {special_number}")


