def show_menu():
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Add Expense (coming soon)")
    elif choice == '2':
        print("View Expenses (coming soon)")
    elif choice == '3':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
