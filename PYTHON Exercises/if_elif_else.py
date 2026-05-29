def assign_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"

    if score >= 90:
        grade = "A"
        remark = "Excellent"
    elif score >= 80:
        grade = "B"
        remark = "Very Good"
    elif score >= 70:
        grade = "C"
        remark = "Good"
    else:
        grade = "F"
        remark = "Needs Improvement"

    return f"Grade: {grade}\nRemark: {remark}"


score = 88

result = assign_grade(score)
print(result)