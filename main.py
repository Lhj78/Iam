import json
from datetime import datetime


class ExpenseManager:
    def __init__(self, file_path='expenses.json'):
        self.file_path = file_path
        self.expenses = []
        self.categories = set(['Groceries', 'Transportation', 'Utilities', 'Entertainment'])
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.expenses = data.get('expenses', [])
                self.categories.update(data.get('categories', []))
        except FileNotFoundError:
            pass  # File doesn't exist yet, start with empty data.
        except json.JSONDecodeError:
            print("Error: Corrupted data file. Starting fresh.")

    def save_data(self):
        with open(self.file_path, 'w') as f:
            json.dump({'expenses': self.expenses, 'categories': list(self.categories)}, f, indent=4)
        print("Data saved successfully.")

    def add_expense(self):
        while True:
            try:
                amount = float(input("Enter amount spent: "))
                if amount <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a positive number for the amount.")

        description = input("Enter a brief description: ")

        print("\nAvailable categories:")
        for i, category in enumerate(sorted(list(self.categories)), 1):
            print(f"{i}. {category}")

        category_choice = input("Select a category number or type a new one: ").strip()
        if category_choice.isdigit():
            categories_list = sorted(list(self.categories))
            if 1 <= int(category_choice) <= len(categories_list):
                category = categories_list[int(category_choice) - 1]
            else:
                print("Invalid category choice. Please try again.")
                return
        else:
            category = category_choice.capitalize()
            self.categories.add(category)
            print(f"New category '{category}' added.")

        date_str = datetime.now().strftime("%Y-%m-%d")
        new_expense = {
            'date': date_str,
            'amount': amount,
            'description': description,
            'category': category
        }
        self.expenses.append(new_expense)
        print("Expense added successfully!")
        self.save_data()

    def view_summary(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        total_spent = 0
        category_summary = {}

        for expense in self.expenses:
            total_spent += expense['amount']
            category = expense['category']
            category_summary[category] = category_summary.get(category, 0) + expense['amount']

        print("\n--- Expense Summary ---")
        print(f"Total Amount Spent: ${total_spent:.2f}\n")
        print("Breakdown by Category:")
        for category, amount in category_summary.items():
            percentage = (amount / total_spent) * 100
            print(f"  - {category}: ${amount:.2f} ({percentage:.1f}%)")
        print("-----------------------")


def main_menu():
    manager = ExpenseManager()
    while True:
        print("\n--- Expense Recording System ---")
        print("1. Add a new expense")
        print("2. View expense summary")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_expense()
        elif choice == '2':
            manager.view_summary()
        elif choice == '3':
            manager.save_data()
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()2