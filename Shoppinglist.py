def menu():
    print("\n Shopping List Manager")
    print("1. Add item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def add_item (shoppinglist):
    item = input("What item do you to add?").lower()
    shoppinglist.append(item)
    print(f"{item} has been added to the list.")


def remove_item (shoppinglist):
    item = input("What item do you to remove?").lower()
    if item in shoppinglist:
        shoppinglist.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} is not in the list")

def view_list(shoppinglist):
    if shoppinglist:
        print("Current shopping list:")
        for item in shoppinglist:
            print(f"- {item}")

def shoppinglist_manager():
    shoppinglist = []

    while True:
        menu()
        choice = input("Enter your choice:")
        if choice == "1":
            add_item(shoppinglist)
        elif choice == "2":
            remove_item(shoppinglist)
        elif choice == "3":
            view_list(shoppinglist)
        elif choice == "4":
            print("Goodbye!")
            return False
        else:
            print("Please type 1, 2, 3 or 4.")

shoppinglist_manager()






