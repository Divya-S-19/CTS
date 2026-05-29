class Employee:
    def __init__(self):
        self.salary = 0

    def set_salary(self, salary):
        if salary <= 0:
            print("Invalid salary")
        else:
            self.salary = salary
        return self

    def apply_raise(self, percent):
        if percent > 0:
            self.salary += self.salary * (percent / 100)
        return self

    def display(self):
        print(f"Final Salary: {self.salary:.2f}")
        return self


emp = Employee()
emp.set_salary(50000).apply_raise(10).display()