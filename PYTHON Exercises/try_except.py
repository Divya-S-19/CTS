def safe_divide(a, b):
    try:
        result = a / b
        return f"Result: {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"


num1 = 10
num2 = 0

output = safe_divide(num1, num2)
print(output)