import json
import tkinter as tk
from tkinter import messagebox, simpledialog

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

# Refresh Listbox
def refresh_listbox():
    contact_listbox.delete(0, tk.END)
    contacts = load_contacts()
    for name in contacts:
        contact_listbox.insert(tk.END, name)

# Add Contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter Name:")
    phone = simpledialog.askstring("Input", "Enter Phone Number:")
    email = simpledialog.askstring("Input", "Enter Email:")
    address = simpledialog.askstring("Input", "Enter Address:")

    if name and phone:
        contacts = load_contacts()
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts(contacts)
        refresh_listbox()
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Warning", "Name and Phone are required!")

# View Contact Details
def view_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact!")
        return

    name = contact_listbox.get(selected[0])
    contacts = load_contacts()
    details = contacts.get(name, {})

    info = f"Name: {name}\nPhone: {details.get('Phone')}\nEmail: {details.get('Email')}\nAddress: {details.get('Address')}"
    messagebox.showinfo("Contact Details", info)

# Update Contact
def update_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact to update!")
        return

    name = contact_listbox.get(selected[0])
    contacts = load_contacts()

    new_phone = simpledialog.askstring("Input", "Enter new Phone:", initialvalue=contacts[name]["Phone"])
    new_email = simpledialog.askstring("Input", "Enter new Email:", initialvalue=contacts[name]["Email"])
    new_address = simpledialog.askstring("Input", "Enter new Address:", initialvalue=contacts[name]["Address"])

    contacts[name] = {"Phone": new_phone, "Email": new_email, "Address": new_address}
    save_contacts(contacts)
    messagebox.showinfo("Success", "Contact updated successfully!")

# Delete Contact
def delete_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact to delete!")
        return

    name = contact_listbox.get(selected[0])
    contacts = load_contacts()

    if messagebox.askyesno("Confirm", f"Are you sure you want to delete {name}?"):
        del contacts[name]
        save_contacts(contacts)
        refresh_listbox()
        messagebox.showinfo("Success", "Contact deleted successfully!")

# Search Contact
def search_contact():
    query = simpledialog.askstring("Search", "Enter Name or Phone Number:")
    contacts = load_contacts()

    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details["Phone"]:
            info = f"Name: {name}\nPhone: {details.get('Phone')}\nEmail: {details.get('Email')}\nAddress: {details.get('Address')}"
            messagebox.showinfo("Contact Found", info)
            return

    messagebox.showwarning("Not Found", "No matching contact found.")

# Create Main Window
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x450")

# Contact Listbox
contact_listbox = tk.Listbox(root, width=50, height=15)
contact_listbox.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

btn_add = tk.Button(btn_frame, text="Add", command=add_contact, width=10)
btn_view = tk.Button(btn_frame, text="View", command=view_contact, width=10)
btn_update = tk.Button(btn_frame, text="Update", command=update_contact, width=10)
btn_delete = tk.Button(btn_frame, text="Delete", command=delete_contact, width=10)
btn_search = tk.Button(btn_frame, text="Search", command=search_contact, width=10)

btn_add.grid(row=0, column=0, padx=5, pady=5)
btn_view.grid(row=0, column=1, padx=5, pady=5)
btn_update.grid(row=1, column=0, padx=5, pady=5)
btn_delete.grid(row=1, column=1, padx=5, pady=5)
btn_search.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Load initial contacts
refresh_listbox()

# Run the app
root.mainloop()
