from datetime import datetime

class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")


tasks = [
    Task("A", "2026-05-30"),
    Task("B", "2026-05-25")
]

tasks.sort(key=lambda x: x.due_date)

for t in tasks:
    print(t.name, t.due_date)