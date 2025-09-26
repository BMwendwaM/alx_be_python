def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            item = input("Enter the item to add: ").strip().lower
            shopping_list.append(item)
            return shopping_list
        elif choice == '2':
            item = input("Enter the item to remove: ").strip().lower
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not in list.")
            return shopping_list
            print(shopping_list)
        elif choice == '3':
            for i in shopping_list:
                print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")
        print(shopping_list)
        
if __name__ == "__main__":
    main()