students = {}

def add_grade(name, grade):
    if grade < 0 or grade > 100:
        return "Invalid grade"

    students.setdefault(name, []).append(grade)


def gpa(grades):
    return sum(grades) / len(grades)


add_grade("Alice", 80)
add_grade("Alice", 90)

print("GPA:", gpa(students["Alice"]))