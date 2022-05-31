# 83/100 in Judge
num_of_lines = int(input())
balanced = False
count_left_bracket = 0
count_right_bracket = 0

for i in range(num_of_lines):
    words = input()

    if words == '(':
        count_left_bracket += 1
    elif words == ')':
        count_right_bracket += 1
    else:
        continue

    if count_left_bracket == count_right_bracket:
        balanced = True
    else:
        balanced = False

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
