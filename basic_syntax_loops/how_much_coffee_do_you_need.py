command = input()
coffee_counter = 0
condition = False

while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee_counter += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee_counter += 2

    if coffee_counter > 5:
        condition = True

    command = input()

if condition:
    print("You need extra sleep")
else:
    print(f"{coffee_counter}")

