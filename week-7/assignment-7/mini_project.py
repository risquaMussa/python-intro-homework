import os
import csv
from datetime import datetime

#Check whether expenses.csv
file_path = "../data/expenses.csv"

if not os.path.exists(file_path):
    print("Error: expenses.csv not found.")
    raise SystemExit
print("expenses.csv found.")

#Read the CSV file
with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    expenses = list(reader)
#print("Expenses data loaded successfully.")
#Convert the amount field to float for each row.
for expense in expenses:
    expense["amount"] = float(expense["amount"])

food_expenses = []

for expense in expenses:
    if expense["category"] == "Food":
        food_expenses.append(expense)

total = 0

for expense in food_expenses:
    total += expense["amount"]

today = datetime.now().strftime("%B %d, %Y")

with open("food_report.txt", "w") as report:
    report.write(f"Food Expense Report — generated {today}\n")

    for expense in food_expenses:
        report.write(f"{expense['date']}: ${expense['amount']:.2f}\n")

    report.write(f"Total: ${total:.2f}\n")

print("Food expense report generated successfully!")
