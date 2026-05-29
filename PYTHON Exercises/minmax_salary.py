def find_salary_range(salaries):
    if len(salaries) == 0:
        return "Salary list is empty"

    lowest = min(salaries)
    highest = max(salaries)

    return f"Lowest Salary: {lowest}\nHighest Salary: {highest}"


salaries = [50000, 75000, 62000, 95000]

result = find_salary_range(salaries)
print(result)