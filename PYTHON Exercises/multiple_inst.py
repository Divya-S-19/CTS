class Employee:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    def display_info(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)
        print()


# Creating multiple objects (instances)
employee1 = Employee("Divya", 101, "HR")
employee2 = Employee("Arun", 102, "IT")
employee3 = Employee("Meena", 103, "Finance")

# Printing employee names
print("Employee Roster")
print("----------------")
print(employee1.name)
print(employee2.name)
print(employee3.name)

print()

# Displaying employee information
employee1.display_info()
employee2.display_info()
employee3.display_info()