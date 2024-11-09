USER_FILE = "user_name.txt"

# Function to register a new user by saving their name to a file.
def register_user(name):
    with open(USER_FILE, "w") as file:
        file.write(name)

# Function to load the user's name from the file.
def get_user_name():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().strip()  # Return the name if it's saved.
    except FileNotFoundError:
        return None  # No user is currently logged in.

# Function to log out the user by deleting the user name file.
def logout_user():
    import os
    # Remove the user name file to log out.
    if os.path.exists(USER_FILE):
        os.remove(USER_FILE)

# Function to get the grocery list file path for a specific user.
def get_user_list_file(user_name):
    return f"{user_name.lower()}_grocery_list.txt"
