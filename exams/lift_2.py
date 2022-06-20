# 100 / 100 Judge
people = int(input())
lifts = list(map(int, input().split(' ')))

total_empty_spaces = 4 * len(lifts)
count_people = 0
for lift in range(len(lifts)):
    while lifts[lift] != 4 and people > 0:
        count_people += 1
        people -= 1
        lifts[lift] += 1

    total_empty_spaces -= lifts[lift]
    if people <= 0:
        break

total_lifts = [str(x) for x in lifts]

if people > total_empty_spaces:
    print(f"There isn't enough space! {people} people in a queue! \n {' '.join(total_lifts)}")
elif people == total_empty_spaces:
    print(' '.join(total_lifts))
elif people < total_empty_spaces:
    print(f"The lift has empty spots!\n {' '.join(total_lifts)}")
