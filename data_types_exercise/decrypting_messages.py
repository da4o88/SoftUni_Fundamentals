key = int(input())
num_of_lines = int(input())
message = ''

for i in range(num_of_lines):
    letters = input()
    new_letter = ord(letters) + key

    message += chr(new_letter)

print(message)
