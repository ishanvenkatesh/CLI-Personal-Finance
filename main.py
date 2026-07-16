expenses = [["Chipotle", "Food", 18.52]]

def main():
    pass

def display_menu():
    print("==== Personal Finance Tracker ====\n")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expenses")
    print("4. Total Spending")
    print("5. Quit")

def add_expense(expense):
    """Takes in list parameter expense and adds it to the list of expenses."""
    expenses.append(expense)

def view_expenses():
    """Lists out all user expenses"""
    for e in expenses:
        for i in e:
            print(i)
        print("")

def search_expenses(search, method):
    """Search parameter is the query. Method is searching by name or category"""
    if method.lower() == "name":
        for e in expenses:
            if e[0].lower() == search.lower():
                print(e)
    elif method.lower() == "category":
        for e in expenses:
            if e[1].lower() == search.lower():
                print(e)
    print("")

        

def calculate_total():
    pass
