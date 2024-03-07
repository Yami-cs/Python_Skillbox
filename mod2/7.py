from flask import Flask, request

app = Flask(__name__)

# Initialize a dictionary to store expenses
storage = {}

@app.route("/add/<date>/<int:number>")
def add_expense(date, number):
    # Parse the date (format: YYYYMMDD)
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])

    # Initialize the dictionary for the year and month
    storage.setdefault(year, {}).setdefault(month, 0)

    # Add the expense to the total for the day
    storage[year][month] += number

    return f"Expense of {number} rubles added for {day}.{month}.{year}"

@app.route("/calculate/<int:year>")
def calculate_year(year):
    # Calculate the total expenses for the year
    total_expenses = sum(storage.get(year, {}).values())
    return f"Total expenses for {year}: {total_expenses} rubles"

@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year, month):
    # Get the expenses for the specified month
    expenses = storage.get(year, {}).get(month, 0)
    return f"Expenses for {month}.{year}: {expenses} rubles"

if __name__ == "__main__":
    app.run()
