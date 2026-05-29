def get_salary(data, dept, employee):
    if dept not in data:
        return "Invalid department"

    if employee not in data[dept]:
        return "Invalid employee"

    return f"Salary: {data[dept][employee]}"


company = {
    "IT": {"Alice": 60000, "Bob": 55000},
    "HR": {"Eve": 50000}
}

result = get_salary(company, "IT", "Alice")
print(result)