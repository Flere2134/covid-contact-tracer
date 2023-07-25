from contact_tracing_app import ContactTracingApp
from contact import Contact
from file_handler import FileHandler
import tkinter as tk
from tkinter import messagebox

def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "User123" and password == "1234":
            return True
        else:
            print("Invalid. Please try again!")

def add_contact_entry():
    name = name_entry.get()
    number = number_entry.get()
    location = location_entry.get()
    date_of_visit = date_of_visit_entry.get()

    app.add_contact(name, number, location, date_of_visit)
    messagebox.showinfo("Contact added")

def search_contact_entry():
    search_term = search_term_entry.get()
    matching_contacts = app.search_contact(search_term)
    if matching_contacts:
        result_text.delete("1.0", tk.END)
        for contact in matching_contacts:
            result_text.insert(tk.END, str(contact), "\n")
    else:
        messagebox.showinfo("Contact not found. Please add contact instead.")

def main():
    if login():
        global app
        app = ContactTracingApp("contacts.txt")

        root = tk.Tk()
        root.title("COVID-19 Contact Tracing App") #title of GUI

        #widgets
        tk.Label(root, text = "Name:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(root, text= "Phone Number:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(root, text= "Location visited:").grid(row=2, column=0, sticky=tk.W)
        tk.Label(root, text= "Date visited:").grid(row=3, column=0, sticky=tk.W)




if __name__ == "__main__":
    main()
