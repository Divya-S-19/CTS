def merge_employee_data(emp1, emp2):
    if not isinstance(emp1, dict) or not isinstance(emp2, dict):
        return "Invalid input"

    emp1.update(emp2)
    return f"Updated Employee Data: {emp1}"


emp1 = {"name": "John", "id": 101}
emp2 = {"department": "IT", "salary": 50000}

result = merge_employee_data(emp1, emp2)
print(result)