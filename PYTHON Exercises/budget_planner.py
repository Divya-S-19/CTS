import matplotlib.pyplot as plt

categories = {
    "Food": 2000,
    "Travel": 1500,
    "Shopping": 3000
}

spent = {
    "Food": 1800,
    "Travel": 2000,
    "Shopping": 2500
}

labels = list(categories.keys())
values = list(spent.values())

plt.pie(values, labels=labels)
plt.title("Budget Overview")
plt.show()

for cat in categories:
    if spent[cat] > categories[cat]:
        print(cat, "Over Budget!")