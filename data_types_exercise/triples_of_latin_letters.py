num = int(input())

start_letter = 97
end_letter = (start_letter + num) - 1

for i in range(start_letter, end_letter + 1):
    for j in range(start_letter, end_letter + 1):
        for k in range(start_letter, end_letter + 1):
            print(f"{chr(i)}{chr(j)}{chr(k)}")
