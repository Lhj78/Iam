The Python code provided implements a simple Expense Recording System that allows users to log and track their daily expenses. It uses object-oriented programming with a class called ExpenseManager to manage all the functionalities, including data persistence, user interaction, and summarization.

How the Project Works
The system operates based on the ExpenseManager class and a main_menu function that serves as the user interface.

1. Data Persistence
__init__: When the program starts, the ExpenseManager object is initialized. It automatically calls the load_data() method to check for a file named expenses.json. This file is used to store all previously recorded expenses and custom categories.

load_data(): This method attempts to open and read the expenses.json file. It uses a try-except block to handle two potential errors:

FileNotFoundError: If the file doesn't exist (e.g., the first time the program is run), the program simply continues without error, starting with an empty list of expenses.

json.JSONDecodeError: If the file is corrupted or not in the correct JSON format, it prints an error message and starts a new, fresh record.

save_data(): This method is called after every new expense is added and when the user chooses to exit. It takes the current expenses list and categories set and writes them to the expenses.json file in a structured JSON format. This ensures that all data is saved and available for the next session.

2. User Interaction and Expense Management
main_menu(): This function presents a simple, text-based menu to the user with three options: add an expense, view a summary, or exit. It uses a while True loop to keep the menu running until the user decides to exit.

add_expense(): When a user chooses to add an expense, this method guides them through the process.

It first uses a while True loop with a try-except block to ensure the user enters a valid, positive number for the expense amount. This is a robust form of input validation.

It then prompts for a description.

Next, it displays the available categories from the self.categories set. The user can either select an existing category by entering its corresponding number or create a new one by typing its name. If a new category is entered, it's automatically added to the self.categories set.

Finally, it creates a new dictionary containing the date, amount, description, and category, and appends it to the self.expenses list. It then calls save_data() to persist the change.

3. Expense Summary
view_summary(): This method generates a report on the user's spending habits.

It first checks if there are any expenses recorded. If not, it prints a message and returns.

It then initializes total_spent to 0 and an empty dictionary called category_summary.

It iterates through the self.expenses list. In each iteration, it adds the expense amount to total_spent and aggregates the amounts by category in the category_summary dictionary.

After the loop, it neatly prints the total amount spent and a breakdown of spending per category, including the percentage of the total that each category represents.
