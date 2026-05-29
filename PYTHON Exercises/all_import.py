from math import *

def math_operations(number):
    if number <= 0:
        return "Invalid input"

    square_root = sqrt(number)
    power_value = pow(number, 2)
    circle_area = pi * number * number

    return (
        f"Number: {number}\n"
        f"Square Root: {square_root:.2f}\n"
        f"Power (square): {power_value}\n"
        f"Circle Area (using radius): {circle_area:.2f}"
    )


number = 9

result = math_operations(number)
print(result)