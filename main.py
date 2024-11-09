import grocery_list
import display_app
import user_data

def main():
    while True:
        # Load the user's name or prompt for registration/login.
        user_name = user_data.get_user_name()
        
        if not user_name:
            user_name = display_app.get_input("Welcome! Please enter your name to register")
            user_data.register_user(user_name)
        
        # Load the user's grocery list.
        list_file = user_data.get_user_list_file(user_name)
        grocery_list.load_grocery_list(list_file)
        
        print(f"\nWelcome back, {user_name}! Your grocery list is ready.")
        
        while True:
            print(f"\n=== {user_name}'s Grocery List App ===")
            display_app.show_menu()
            choice = display_app.get_input("Select an option")
            
            if choice == "1":
                item = display_app.get_input("Enter item to add")
                print(grocery_list.add_item(item))
            
            elif choice == "2":
                item = display_app.get_input("Enter item to cross out")
                print(grocery_list.cross_out_item(item))
            
            elif choice == "3":
                list_content = grocery_list.view_list()
                display_app.show_grocery_list(list_content)
            
            elif choice == "4":
                print(f"Saving your list, {user_name}.")
                grocery_list.save_grocery_list(list_file)
                print(f"Exiting {user_name}'s Grocery List App. Goodbye!")
                return  # End the program after saving.
            
            elif choice == "5":
                print(f"Logging out {user_name}...")
                grocery_list.save_grocery_list(list_file)
                user_data.logout_user()
                break  # Return to the main login/register loop.
            
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
