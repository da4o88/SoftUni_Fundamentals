name = input()
condition = True

while name != "Welcome!":
    if name == "Voldemort":
        condition = False
        print("You must not speak of that name!")
        break
    else:
        if len(name) < 5:
            print(f"{name} goes to Gryffindor.")
        elif len(name) == 5:
            print(f"{name} goes to Slytherin.")
        elif len(name) == 6:
            print(f"{name} goes to Ravenclaw.")
        else:
            print(f"{name} goes to Hufflepuff.")

    name = input()

if condition:
    print("Welcome to Hogwarts.")

