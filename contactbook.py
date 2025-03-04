import json

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts = load_contacts()
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts(contacts)

    print(f"Contact for {name} added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for name, details in contacts.items():
        print(f"{name} - {details['Phone']}")

# Search for a contact
def search_contact():
    query = input("Enter Name or Phone Number to search: ")
    contacts = load_contacts()

    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details["Phone"]:
            print("\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            return

    print("No matching contact found.")

# Update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    contacts = load_contacts()

    if name in contacts:
        print("\nWhat do you want to update?")
        print("1. Phone Number")
        print("2. Email")
        print("3. Address")
        choice = input("Enter your choice: ")

        if choice == "1":
            contacts[name]["Phone"] = input("Enter new Phone Number: ")
        elif choice == "2":
            contacts[name]["Email"] = input("Enter new Email: ")
        elif choice == "3":
            contacts[name]["Address"] = input("Enter new Address: ")
        else:
            print("Invalid choice.")
            return

        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main menu
def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
