import math

def calculate_circle_area(radius):
    if radius <= 0:
        return "Invalid radius"

    area = math.pi * radius * radius
    return f"Area of Circle: {area:.2f}"


radius = 7

result = calculate_circle_area(radius)
print(result)