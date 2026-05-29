def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Invalid operator"

    except ZeroDivisionError:
        return "Error: Division by zero"


try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+,-,*,/): ")

    result = calculate(a, b, op)
    print("Result:", result)

except ValueError:
    print("Invalid input")