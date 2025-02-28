import json

def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Added expenses: {description}, Amount: {amount}")

def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense['amount']
    return sum

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)


def show_budget_details(budget, expenses):
    print(f"Total budget: {budget}\n Expenses:")
    for expense in expenses:
        print(f"{expense['description']}: {expense['amount']}")
    print(f"Total Spent: {get_total_expenses(expenses)}")
    print(f"Remaining Budget: {get_balance(budget, expenses)}")

def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, [] # handling error with empty list

def save_budget_detail(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    print('Welcome to the Budget Tracker')
    filepath = 'budget_data.json' # define the path of your json file
    initial_budget, expenses = load_budget_data(filepath)
    if initial_budget == 0:
        initial_budget = float(input('Please enter your initial budget: '))
    budget = initial_budget

    while True:
        print("\nWhat would like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = int(input('Enter your number out of 1,2,3,4: '))

        if choice == 1:
            description = input("Enter expense description: ")
            amount = float(input("Enter your amount: "))
            add_expense(expenses, description, amount)
        elif choice == 2:
            show_budget_details(budget, expenses)
        elif choice == 3:
            save_budget_detail(filepath, initial_budget, expenses)
            print('Exiting program.....\n bye ')
            break
        else:
            print('Invite choice, please chose again')



if __name__ == "__main__":
    main()