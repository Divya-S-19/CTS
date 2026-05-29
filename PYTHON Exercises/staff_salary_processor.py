import csv

employees = []

try:
    # Read CSV file
    with open("staff_salary.csv", "r") as file:
        reader = csv.DictReader(file)

        # Convert rows into list of dictionaries
        for row in reader:
            row["Salary"] = int(row["Salary"])
            employees.append(row)

    # Filter employees with salary > 50000
    high_salary_employees = [
        employee for employee in employees
        if employee["Salary"] > 50000
    ]

    # Calculate average salary
    total_salary = sum(employee["Salary"] for employee in employees)
    average_salary = total_salary / len(employees)

    # Print filtered employees
    print("Employees with Salary > 50000")
    print("-----------------------------")

    for employee in high_salary_employees:
        print(employee["Name"], "-", employee["Salary"])

    # Print average salary
    print("\nAverage Salary:", average_salary)

except FileNotFoundError:
    print("Error: staff_salary.csv file not found.")

except ValueError:
    print("Error: Invalid salary data in CSV file.")