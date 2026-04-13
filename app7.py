contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone
    print("Contact added!")

def view_contacts():
    for name, phone in contacts.items():
        print(name, ":", phone)

def search_contact():
    name = input("Enter name to search: ")
    print(contacts.get(name, "Not found"))

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Deleted")
    else:
        print("Not found")

def menu():
    while True:
        print("\n1. Add\n2. View\n3. Search\n4. Delete\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

menu()