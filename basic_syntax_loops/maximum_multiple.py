divisor = int(input())
number_boundary = int(input())

for i in range(number_boundary, 0, -1):
    if i % divisor == 0:
        print(i)
        break

