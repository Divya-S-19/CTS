def check_pass(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks"

    if marks >= 40:
        return "Pass"


marks = 75

result = check_pass(marks)
print(result)