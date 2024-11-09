# Function to display the main menu of the app.
def show_menu():
    # Print the menu options to the console.
    print("\n=== Grocery List App ===")
    print("1. Add item")
    print("2. Cross out item")  # Updated to "Cross out" instead of "Remove item"
    print("3. View list")
    print("4. Exit")
    print("5. Logout")  # New option for logging out
    print("========================")

# Function to get user input with a prompt.
def get_input(prompt):
    # Prompt the user and return their input.
    return input(f"\n{prompt}: ")

# Function to display the grocery list in a readable format.
def show_grocery_list(list_content):
    # Print the grocery list with a heading.
    print("\n=== Your Grocery List ===")
    # If the list has content, print the items.
    if list_content:
        print(list_content)
    else:
        # If the list is empty, notify the user.
        print("Your list is empty.")
    print("=========================")
