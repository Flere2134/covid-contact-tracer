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

def main():
    if login():
        app = ContactTracingApp("contacts.txt")

        while True:
            print("\nCOVID Contact Tracing App\n1. Add a Contact\n2. Search a Contact\n3. Exit")

            choose = input("Enter your choice: ")

            if choose == "1":
                name = input("Enter Name: ")
                number = input("Enter Phone Number: ")
                location = input("Enter Location visited: ")
                date_of_visit = input("Enter the date visited: ")
                app.add_contact(name, number, location, date_of_visit)
            elif choose == "2":
                search_term = input("Enter Contact Name or Phone Number: ")
                matching_contacts = app.search_contact(search_term)
                if matching_contacts:
                    print("\nMatching Contacts:")
                    for contact in matching_contacts:
                        print(contact)
                else:
                    print("No matched contact found")
            elif choose == "3":
                break
            else:
                print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()
