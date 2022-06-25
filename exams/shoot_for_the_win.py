targets = list(map(int, input().split(' ')))
command = input()
count = 0
shooted_targets = []


def index_in_list(a_list, index):
    return (index < len(a_list))


while command != "End":
    shoot = int(command)

    # Check does index is correct and shoot the target
    target_down = index_in_list(targets, shoot)

    if target_down and shoot not in shooted_targets:
        # Value of current target which is shooted
        current_target = targets[shoot]
        targets[shoot] = -1
        count += 1
        shooted_targets.append(shoot)

        for i in range(len(targets)):
            if targets[i] == -1:
                continue
            elif targets[i] > current_target:
                targets[i] -= current_target
            elif targets[i] <= current_target:
                targets[i] += current_target

    command = input()


final_targets = [str(s) for s in targets]
print(f"Shot targets: {count} -> {' '.join(final_targets)}")
