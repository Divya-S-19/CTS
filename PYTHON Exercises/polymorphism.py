class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer writes code")


class Tester(Employee):
    def work(self):
        print("Tester tests software")


employees = [Developer(), Tester(), Employee()]

for e in employees:
    e.work()