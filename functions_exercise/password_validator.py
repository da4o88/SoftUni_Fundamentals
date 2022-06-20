password = input()


def valid_password(password):
    condition = True
    pass_valid = True
    letters = 0
    digits = 0
    characters = 0

    for ch in password:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1
        else:
            condition = False
            characters += 1

    characters += letters + digits

    if characters < 6 or characters > 10:
        print("Password must be between 6 and 10 characters")
        pass_valid = False

    if not condition:
        print("Password must consist only of letters and digits")
        pass_valid = False

    if digits < 2:
        print("Password must have at least 2 digits")
        pass_valid = False

    return pass_valid


check_password = valid_password(password)

if check_password:
    print("Password is valid")
