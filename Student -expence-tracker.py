# Student-expence-tracker
A simple python program to track daily students expenses and remaining budget 
# Personal Expense Tracker - Built by Aleena (1st Year BCA)

print("=== Student Daily Expense Tracker ===")
budget = float(input("Enter your monthly pocket money / budget (Rs): "))
expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View All Expenses & Balance")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        item = input("What did you spend on? (e.g., Snacks, Bus, Book): ")
        amount = float(input(f"Enter amount for {item} (Rs): "))
        expenses.append((item, amount))
        print("Expense added successfully!")

    elif choice == "2":
        print("\n--- Your Expense Summary ---")
        total_spent = 0
        for item, amount in expenses:
            print(f"- {item}: Rs {amount:.2f}")
            total_spent += amount

        balance = budget - total_spent
        print(f"Total Spent: Rs {total_spent:.2f}")
        print(f"Remaining Balance: Rs {balance:.2f}")

        if balance < 0:
            print("Alert: You have crossed your budget!")

    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
