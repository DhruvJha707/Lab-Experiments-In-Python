'''Create a contact book where users can store, search, update, and delete contacts. Use 
dictionary for storing contacts. '''

contacts = {}

while True:
    print("\n*** Contact Book Menu ***")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact added successfully!")

    elif choice == 2:
        name = input("Enter name to search: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found.")

    elif choice == 3:
        name = input("Enter name to update: ")
        if name in contacts:
            number = input("Enter new phone number: ")
            contacts[name] = number
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == 5:
        print("\n--- All Contacts ---")
        for name, number in contacts.items():
            print(name, ":", number)

    elif choice == 6:
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
