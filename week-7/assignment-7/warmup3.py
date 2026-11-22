#Warmup 3: Use the os Module
import os

print(os.getcwd())


if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

#build path
path = os.path.join("..", "data", "expenses.csv")
print(path)