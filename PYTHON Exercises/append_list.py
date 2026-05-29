def add_expense(expenses, amount):
    if not isinstance(expenses, list):
        return "Invalid list"

    if not isinstance(amount, (int, float)) or amount <= 0:
        return "Invalid expense amount"

    expenses.append(amount)
    return f"Updated Expenses: {expenses}"


expenses = [500, 1200, 300]

result = add_expense(expenses, 450)
print(result)