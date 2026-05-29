def area(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        return "Invalid input"

    if length <= 0 or width <= 0:
        return "Invalid dimensions"

    return length * width


result = area(5, 3)
print("Area:", result)