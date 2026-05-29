import json

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def __str__(self):
        return f"{self.name} ({self.emp_id}) - {self.salary}"


employees = {
    1: {"name": "Alice", "salary": 60000},
    2: {"name": "Bob", "salary": 55000}
}

# Save to file
with open("emps.json", "w") as f:
    json.dump(employees, f)

# Load from file
with open("emps.json", "r") as f:
    data = json.load(f)

print("Employees:")
for emp_id, info in data.items():
    print(emp_id, info)