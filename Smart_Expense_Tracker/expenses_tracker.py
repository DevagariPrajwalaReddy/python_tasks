import json
import datetime

def log_and_time(func):
    def wrapper():
        start_time = datetime.datetime.now()
        print(f"Function '{func.__name__}' started at {start_time}")
        func()
        end_time = datetime.datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        with open('app_log.txt', 'a') as f:
            f.write(f"{start_time} - Function '{func.__name__}' executed in {execution_time}s\n")
        print(f"Function '{func.__name__}' executed in {execution_time}s")
    return wrapper

# Add daily expenses

@log_and_time
def add_expense():
     # here expenses - holds - expense added by the user - in - list form
    try:
        with open('expenses.json', 'r') as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []           
    
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date: # if date is not given by user it considers today as date
        date = datetime.date.today().isoformat() # date is considered in iso format (yyyy-mm-dd)
    else:
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Please enter date in valid format!")
            return
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    })
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f, indent=4)
    print("Expense added successfully!")

# View all expenses

@log_and_time
def view_expenses():
    try:
        with open('expenses.json', 'r') as f:
            expenses = json.load(f)
    except FileNotFoundError:
        print("No expenses recorded yet.")
        return
    
    expenses.sort(key=lambda x: x['date']) # ascending order of dates
    total_expenditure = sum(expense['amount'] for expense in expenses)
    print("Expenses:")
    for expense in expenses:
        print(f"""Date: {expense['date']}, 
              Category: {expense['category']}, 
              Amount: {expense['amount']}, 
              Description: {expense['description']}""")
    print(f"Total Expenditure: {total_expenditure}")

@log_and_time
def monthly_summary():
    try:
        with open('expenses.json', 'r') as f:
            expenses = json.load(f)
    except FileNotFoundError:
        print("No expenses recorded yet.")
        return
    

    month = int(input("Enter month (MM): "))
    # validating month
    if month<1 or month>12:
        print("Please enter valid month.")
        return
    
    year = int(input("Enter year (YYYY): "))
    monthly_expenses = []
    for expense in expenses:
        dt = datetime.datetime.strptime(expense['date'], '%Y-%m-%d') 
        # strptime - stringparse time- converts string representation of date into date time object-
        # takes 2 args - string that represents date and pattern
        if dt.month == month and dt.year == year:
            monthly_expenses.append(expense)
    if not monthly_expenses:
        print("No records found for the given month and year.")
        return
    summary = {}
    for expense in monthly_expenses:
        category = expense['category']
        if category in summary:
            summary[category] += expense['amount']
        else:
            summary[category] = expense['amount']
    print(f"Monthly Summary: {datetime.date(year, month, 1).strftime('%B')} {year}")
    # datetime.date(year, month, 1).strftime('%B') -- formats month number as full month name
    for category, amount in summary.items():
        print(f"{category}: ₹{amount}")
    print(f"Total: ₹{sum(summary.values())}")

while True:
    print("Smart Expense Tracker")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Monthly Summary")
    print("4. Exit")
    choice = input("Enter your choice(1/2/3/4): ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        monthly_summary()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

