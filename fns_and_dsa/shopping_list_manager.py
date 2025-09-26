shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input(int("Enter your choice: "))
        
        if choice == '1':
            item =  input("Item name:")
            shopping_list.append(item)
            # Prompt for and add an item
            print(f"{item} has been added to shopping list")
            
        elif choice == '2':
            # Prompt for and remove an item
            item =  input("Item name: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from shopping list")
            else:
                print(f"{item} not found in shopping list")

        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()