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
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            item = input("Enter the item to add: ").strip().lower()
            shopping_list.append(item)
            print(f"You added, {item}")
        elif choice == '2':
            item = input("Enter the item to remove: ").strip().lower()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"You removed, {item}.")
            else:
                print("Item not in list.")
        elif choice == '3':
            for i in shopping_list:
                print(i)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    return shopping_list
        
if __name__ == "__main__":
    main()