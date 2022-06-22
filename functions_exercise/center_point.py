import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def closest_distance_to_center(a, b):
    c = math.sqrt((a ** 2) + (b ** 2))

    return c


first_point_distance = closest_distance_to_center(x1, y1)
second_point_distance = closest_distance_to_center(x2, y2)

if first_point_distance > second_point_distance:
    x = x2
    y = y2
elif first_point_distance < second_point_distance:
    x = x1
    y = y1
else:
    x = x1
    y = y1

x = math.floor(x)
y = math.floor(y)

print(f'({x}, {y})')

