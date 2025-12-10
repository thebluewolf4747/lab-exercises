import json
import os

DB_FILENAME = "Text Files/contacts.json"
def load_contacts(filename):

    if not os.path.exists(filename):
        print(f"[INFO] No database found at {filename}. Starting fresh.")
        return {}
    
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"[CRITICAL] Data corruption in {filename}. Backup restored.")
        return {}

def save_contacts(contacts):
    with open(DB_FILENAME, "w") as f:
        json.dump(contacts, f)

def add_contact(contacts: dict) -> None:
    name = input("Name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    number = input("Number: ")
    if not number:
        print("Error: Number cannot be empty.")
        return
    contacts[name] = number
    print(f"{name} added!")
    save_contacts(contacts)
    return contacts

def view_contacts(contacts):
    for key, value in contacts.items():
        print(f"Name: {key}, Phone Number: {value}")

def delete_contact(contact, contacts):
    if contact in contacts:
        del[contact.keys]
    
    return contacts

contacts = load_contacts("Text Files/contacts.json")
running = True
while running:
    choice = input("1. Add, 2. View, 3. Save, 4. Delete,  5. Quit: ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        view_contacts(contacts)

    elif choice == "3":
        save_contacts(contacts)
        break

    elif choice == "4":
        contact = input("What is the name of the contact you want to delete? ")
        delete_contact(contact, contacts)
        save_contacts(contacts)
        break

    elif choice == "5":
        running = False

