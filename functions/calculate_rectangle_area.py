# Create a function that calculates and returns the area of a rectangle by given width and height.
# Print the result on the console.

def rectangle_area(width, height):
    return width * height


width = int(input())
height = int(input())

result = rectangle_area(width, height)

print(result)
