numbers = list(map(int, input().split(' ')))

time_car1 = 0
time_car2 = 0

car1 = numbers[: len(numbers) // 2 + 1]
car2 = numbers[len(numbers) // 2:]

# First car time
for i in range(len(car1) - 1):

    if car1[i] == 0:
        time_car1 *= 0.8

    time_car1 += car1[i]

# Second car time

for j in range(len(car2) - 1, 0, -1):

    if car2[j] == 0:
        time_car2 *= 0.8

    time_car2 += car2[j]

if time_car1 < time_car2:
    car = 'left'
    print(f"The winner is {car} with total time: {time_car1:.1f}")
else:
    car = 'right'
    print(f"The winner is {car} with total time: {time_car2:.1f}")
