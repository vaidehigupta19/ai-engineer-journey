contacts = {}

while True:
    print("------Contact Book------")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Input your choice (1-5) : ")

    if choice == "1":
        name = input("Enter contact name : ")
        phone = input("Enter contact number : ")
        contacts[name] = phone
        print("Contacts phone added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContacts:")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")

    elif choice == "3":
        name = input("Enter contact name to search")
        if name in contacts:
            print(f"{name}'s phone number is {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact you want to delete")
        if name in contacts:
            del contacts[name]
            print("Contact is deleted")
        else:
            print("Not found")

    elif choice == "5":
        print("Thank you for using Contact book!")
        break
else:
    print("Invalid choice.")
