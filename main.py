expenses = []

def main():
    while True:
        display_menu()
        choice =  int(input("Enter a num: "))
        print("")
        if choice == 1:
            name = input("Enter expense name: ")
            category = input("Enter expense category: ")
            cost = float(input("Enter expense cost: "))
            add_expense([name, category, cost])
            print("Expense added.\n")
        elif choice == 2:
            print("Expense list: \n")
            view_expenses()
        elif choice == 3:
            method = input("Search by name or category: ")
            search = input("What is your search query: ")
            print(search_expenses(search, method))
            print("")
        elif choice == 4: 
            print(f"Total expenses: {calculate_total()}")
            print("")
        elif choice == 5:
            print("Goodbye.")
            break
        else:
            print("Not a valid input.\n")


def display_menu():
    print("==== Personal Finance Tracker ====\n")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expenses")
    print("4. Total Spending")
    print("5. Quit\n")

def add_expense(expense):
    """Takes in list parameter expense and adds it to the list of expenses."""
    expenses.append(expense)

def view_expenses():
    """Lists out all user expenses"""
    i = 1
    for e in expenses:     
        print(str(i))
        print(f"Name: {e[0]}")
        print(f"Category: {e[1]}")
        print(f"Cost: {e[2]}\n")
        i += 1

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
    if result == []:
        return "No matching expenses found"
    return result    

def calculate_total():
    """Calculates the total expenses"""
    total = 0
    for e in expenses:
        total += e[2]
    return total


main()

