grocery_list = []

# Function to load a user's grocery list from their file.
def load_grocery_list(file_path):
    global grocery_list
    grocery_list = []  # Clear the current list.
    try:
        with open(file_path, "r") as file:
            for line in file:
                # Each line is an item in the format "item_name,completed_status".
                item, status = line.strip().split(",")
                grocery_list.append((item, status == "True"))
    except FileNotFoundError:
        pass  # If the file doesn't exist, the list stays empty.

# Function to save the current grocery list to the user's file.
def save_grocery_list(file_path):
    with open(file_path, "w") as file:
        for item, completed in grocery_list:
            file.write(f"{item},{completed}\n")

# Function to add an item to the grocery list.
def add_item(item):
    grocery_list.append((item, False))  # Add the item as not completed.
    return f"{item} added to the list."

# Function to cross out (check off) an item in the grocery list.
def cross_out_item(item):
    for i, (name, completed) in enumerate(grocery_list):
        if name == item:
            grocery_list[i] = (name, True)
            return f"{item} has been crossed out."
    return f"{item} not found in the list."

# Function to view all items in the grocery list.
def view_list():
    if not grocery_list:
        return "Your grocery list is empty."
    
    formatted_list = []
    for i, (item, completed) in enumerate(grocery_list):
        if completed:
            formatted_list.append(f"{i + 1}. ~~{item}~~ (crossed out)")
        else:
            formatted_list.append(f"{i + 1}. {item}")
    
    return "\n".join(formatted_list)
