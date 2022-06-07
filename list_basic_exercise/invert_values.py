numbers = input()
origin_list = numbers.split(' ')
invert_list = []

for i in range(len(origin_list)):
    temp_number = int(origin_list[i]) * (-1)
    invert_list.append(temp_number)

print(invert_list)
