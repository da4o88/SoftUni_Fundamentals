# Testing for sum of elements in nested list
list = [[1, 2, 3], [4, 5, 6]]

sum = 0

sum_list = []
for l in list:
    for element in l:
        sum += element
    print(sum)
    sum_list.append(sum)
    sum = 0

