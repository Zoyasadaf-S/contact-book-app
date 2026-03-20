# Contact Book Application
# Features:
# Add contact
# Store contacts in file
# Search contact
# Display contacts

contacts = {}

def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        pass

def add_contact():
    name = input("Enter Name: ")
    phone = int(input("Enter contact number: "))
    if name in contacts or phone in contacts.values():
        print("This contact already exists!!!!")
    else:
        contacts[name] = phone
        print("Contact addedd successfully!!!!")

def save_contacts():
    with open("contacts.txt","w") as file:
        for name, phone in contacts.items():
            file.write(name + ","+ phone +"\n")

def view_contacts():
    if not contacts:
        print("Contacts not exists!!!!")
    else:
        print("Contacts List:")
        for name, phone in contacts.items():
            print(name, ' - ', phone)

def update_contacts():
    u_name = input("Enter the name of the contact to be updated: ")
    if u_name not in contacts:
        print("No contact found!!")
    else:
        u_phone = input("Enter a new number: ")
        contacts[u_name] = u_phone
        print("Contact updated successfully!!!!")

def search_contacts():
    s_name = input("Enter the name u want to search: ")
    if s_name not in contacts:
        print("Contact not found!!!!")
    else:
        print(s_name ," - ",contacts[s_name])

def delete_contacts():
    d_name = input("Enter the name of contact you want to delete: ")
    if d_name in contacts:
        del contacts[d_name]
        print("Contact deleted successfully!!!!")
    else:
        print("Error ocurred!! contact couldn\'t be deleted!!!!")

def menu():
    load_contacts()

    while True:
        print("\n==== Contact Book ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            delete_contacts()
        elif choice == "5":
            update_contacts()
        elif choice == "6":
            save_contacts()
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice.")

menu()
