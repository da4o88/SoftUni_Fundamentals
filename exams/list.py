# 70/100 in judge
passengers = int(input())
lifts = list(map(int,  input().split(' ')))

counter = 0
condition = False
empty_wagons = False

for j in lifts:
    counter += j

if passengers < (4 * len(lifts)):
    empty_wagons = True

for i in range(len(lifts)):
    while lifts[i] < 4:
        if passengers == 0:
            condition = True
            break
        lifts[i] += 1
        passengers -= 1

    if condition:
        break


lifts = [str(l) for l in lifts]

if empty_wagons:
    print(f"The lift has empty spots!")
    print(' '.join(lifts))
elif passengers > 0:
    print(f"There isn't enough space! {passengers} people in a queue!")
    print(' '.join(lifts))
else:
    print(' '.join(lifts))
