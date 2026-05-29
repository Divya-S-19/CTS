from datetime import datetime
import csv

expenses = {}

# Get current month and year
current_month = datetime.now().month
current_year = datetime.now().year

try:
    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Convert date string to datetime object
            expense_date = datetime.strptime(row["date"], "%Y-%m-%d")

            # Filter only current month expenses
            if (
                expense_date.month == current_month
                and expense_date.year == current_year
            ):
                category = row["category"]
                amount = float(row["amount"])

                # Group expenses by category
                if category not in expenses:
                    expenses[category] = 0

                expenses[category] += amount

    # Print summary
    print("Current Month Expense Summary")
    print("-----------------------------")

    for category, total in expenses.items():
        print(category, ":", total)

except FileNotFoundError:
    print("Error: expenses.csv file not found.")

except ValueError:
    print("Error: Invalid data in CSV file.")