year = int(input())
condition = False
while not condition:
    year += 1

    num = str(year)

    count = 0
    for i in range(len(num)):
        count = 0
        for j in range(i + 1, len(num)):
            if num[i] == num[j]:
                count += 1
                break
        if count >= 1:
            break

    if count == 0:
        condition = True

print(year)
