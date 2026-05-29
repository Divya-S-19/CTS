def display_coordinates(coordinates):
    if len(coordinates) != 2:
        return "Invalid coordinates"

    x, y = coordinates

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "Coordinates must be numbers"

    return f"X Coordinate: {x}, Y Coordinate: {y}"


coordinates = (10, 20)

result = display_coordinates(coordinates)
print(result)