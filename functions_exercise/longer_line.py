import math
first_point_x1 = float(input())
first_point_y1 = float(input())
first_point_x2 = float(input())
first_point_y2 = float(input())
second_point_x1 = float(input())
second_point_y1 = float(input())
second_point_x2 = float(input())
second_point_y2 = float(input())

x, y, x1, y1 = 0, 0, 0, 0


# Find which line is longer
def line_distance_between_two_points(a1, b1, a2, b2):
    a = a2 - a1
    b = b2 - b1
    c = math.sqrt((a ** 2) + (b ** 2))

    return c


# Find which point is closest to center
def closest_distance_to_center(a, b):
    c = math.sqrt((a ** 2) + (b ** 2))

    return c


# Which pair of points have longer distance
first_line_distance = line_distance_between_two_points(first_point_x1, first_point_y1, first_point_x2, first_point_y2)
second_line_distance = line_distance_between_two_points(second_point_x1, second_point_y1,
                                                        second_point_x2, second_point_y2)

# Check longer distance and closest point to center
if first_line_distance < second_line_distance:
    first_point_distance = closest_distance_to_center(second_point_x1, second_point_y1)
    second_point_distance = closest_distance_to_center(second_point_x2, second_point_y2)

    if first_point_distance > second_point_distance:
        x = second_point_x2
        y = second_point_y2
        x1 = second_point_x1
        y1 = second_point_y1

    elif first_point_distance < second_point_distance:
        x = second_point_x1
        y = second_point_y1
        x1 = second_point_x2
        y1 = second_point_y2


elif first_line_distance >= second_line_distance:
    first_point_distance = closest_distance_to_center(first_point_x1, first_point_y1)
    second_point_distance = closest_distance_to_center(first_point_x2, first_point_y2)

    if first_point_distance > second_point_distance:
        x = first_point_x2
        y = first_point_y2
        x1 = first_point_x1
        y1 = first_point_y1

    elif first_point_distance <= second_point_distance:
        x = first_point_x1
        y = first_point_y1
        x1 = first_point_x2
        y1 = first_point_y2


x = math.floor(x)
y = math.floor(y)
x1 = math.floor(x1)
y1 = math.floor(y1)

print(f"({x}, {y})({x1}, {y1})")
