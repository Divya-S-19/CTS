def show_coordinates(coords):
    if not isinstance(coords, tuple):
        return "Invalid input"

    x, y = coords

    return f"Coordinates: ({x}, {y})"


coords = (10, 20)

result = show_coordinates(coords)
print(result)