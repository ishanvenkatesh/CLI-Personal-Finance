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
    result = []
    if method.lower() == "name":
        for e in expenses:
            if e[0].lower() == search.lower():
                result.append(e)
    elif method.lower() == "category":
        for e in expenses:
            if e[1].lower() == search.lower():
                result.append(e)
    for e in result:
        print(str(e) + "\n")
        

def calculate_total():
    """Calculates the total expenses"""
    sum = 0
    for e in expenses:
        sum += e[2]
    return sum


add_expense(["Gas", "Transportation", 12.00])
view_expenses()
print(search_expenses("Gas", "name"))
print(calculate_total())


