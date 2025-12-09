import json
def load_contacts():
    try:
        with open("Text Files/contacts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {} # Return empty dict if no file exists

def save_contacts(contacts):
    with open("Text Files/contacts.json", "w") as f:
        json.dump(contacts, f)

def add_contact(contacts):
    name = input("Name: ")
    number = input("Number: ")
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

contacts = load_contacts()
while True:
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

