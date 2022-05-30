number_of_letters = int(input())
sum = 0

for i in range(number_of_letters):
    char = input()
    char = ord(char)

    sum += char

print(f"The sum equals: {sum}")
