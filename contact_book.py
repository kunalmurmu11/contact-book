import json
import os

FILE_NAME = "contacts.json"

# Load contacts
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save contacts
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("Contact added ✅")

# View contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found 📭")
        return

    print("\nContacts List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")

# Search contact
def search_contact(contacts):
    keyword = input("Enter name to search: ").lower()
    found = False

    for contact in contacts:
        if keyword in contact["name"].lower():
            print(f"{contact['name']} | {contact['phone']} | {contact['email']}")
            found = True

    if not found:
        print("No contact found ❌")

# Delete contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to delete: "))
        if 1 <= index <= len(contacts):
            removed = contacts.pop(index - 1)
            save_contacts(contacts)
            print(f"Deleted: {removed['name']} ❌")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter a valid number!")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()