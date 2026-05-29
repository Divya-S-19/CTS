import csv

# List to store employee records
employees = []

# Read CSV file
with open("employees.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)

    # Convert rows into list of dictionaries
    for row in csv_reader:
        # Convert salary to integer
        row["salary"] = int(row["salary"])
        employees.append(row)

# Filter employees with salary > 50000 using list comprehension
high_salary_employees = [
    emp for emp in employees if emp["salary"] > 50000
]

# Print filtered employees
print("Employees with salary greater than 50000:\n")
for emp in high_salary_employees:
    print(emp)

# Calculate average salary
total_salary = sum(emp["salary"] for emp in employees)
average_salary = total_salary / len(employees)

# Print average salary
print("\nAverage Salary:", average_salary)