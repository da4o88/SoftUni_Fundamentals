energy = int(input())
distance = input()
battle_wins = 0
no_energy = False

while distance != 'End of battle':

    lost_energy = int(distance)

    if energy >= lost_energy:

        energy -= lost_energy
        battle_wins += 1

        if battle_wins % 3 == 0:
            energy += battle_wins

    else:
        no_energy = True
        break

    distance = input()

if no_energy:
    print(f"Not enough energy! Game ends with {battle_wins} won battles and {energy} energy")
else:
    print(f"Won battles: {battle_wins}. Energy left: {energy} ")
