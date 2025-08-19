import json
from datetime import datetime

Expenses_file = 'expenses.json'

def load_expenses():
    '''
        It is used to load expenses from json file
    '''
    try:
        with open(Expenses_file,'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # It handles the case where a file doesn't exists/corrupted
        return []
        #returns an empty list is not file present

def save_expenses(expenses):
    '''Used to save the user defined expenses to json file
    '''
    with open(Expenses_file, 'w') as file:
        json.dump(expenses, file, indent=4)
    print("Expenses saved Successfully!!")


def add_expense():
    '''Used to allow users to add any new expenses'''
    expenses = load_expenses()
    try:
        amount = float(input("Enter the amount you spent: $"))
        category = input("Enter the category(e.g. Food,Transport,Entertainment,etc..): ").capitalize()
        date = datetime.now().strftime("%Y-%m-%d")
        new_expense = {
            "Amount": amount,
            "Category": category,
            "Date": date
        }
        expenses.append(new_expense)
        save_expenses(expenses)
        print(f"Expense of ${amount:.2f} for '{category}' on {date} added.")
    except ValueError:
        print("Invaid amount.Please enter a number.")

def view_summaries():
    '''Used to display the spending of the user'''
    expenses = load_expenses()
    if not expenses:
        print("No history of expenses.")
        return
    #If the expenses are present then we use the following
    total_spends = sum(item['Amount'] for item in expenses)
    print(f"\nTotal spendings: ${total_spends:.2f}")

    #Used to display spendings using categories
    category_sum = {}
    for item in expenses:
        category = item['Category']
        amount = item['Amount']
        category_sum[category] = category_sum.get(category, 0) + amount
    
    print("\n--Expenses by categories--")
    for category, total in category_sum.items():
        print(f"{category}: ${total:.2f}")
    
    #Used to display daily expenses summary
    daily_expenses = {}
    for item in expenses:
        date = item['Date']
        amount = item['Amount']
        daily_expenses[date] = daily_expenses.get(date, 0) + amount

    print("\n-- Daily Expenses --")
    for date, total in sorted(daily_expenses.items()):
        print(f"{date}: ${total:.2f}")


def main_function():
    '''
        This function is used to display main menu and 
        the user inputs
    '''
    while True:
        print("\n----Personal Expense Tracker----\n")
        print("1. Add a new expense ")
        print("2. View summaries")
        print("3. Exit")
        choice = input("Enter your choice or option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summaries()
        elif choice == '3':
            print("Thank you for using Expense Tracker!!")
            break
        else:
            print("Invalid choice. Please try again...")

if __name__ == "__main__":
    main_function()
