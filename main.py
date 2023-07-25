from contact_tracing_app import ContactTracingApp
from contact import Contact
from file_handler import FileHandler
import tkinter as tk
from tkinter import messagebox

def login():
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "User123" and password == "1234":
            login_window.destroy()
            main.app()
        else:
            messagebox.showerror("INVALID INPUT. PLEASE TRY AGAIN!")

login_window = tk.Tk()
login_window.geometry("200x150")
login_window.title("User Login")

tk.Label(login_window, text = "Username:", font = ("Helveltica", 10)).pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text = "Password:", font = ("Helveltica", 10))
password_entry = tk.Entry(login_window)
password_entry.pack()
    

def add_contact_entry():
    name = name_entry.get()
    number = number_entry.get()
    location = location_entry.get()
    date_of_visit = date_entry.get()

    app.add_contact(name, number, location, date_of_visit)
    messagebox.showinfo("Contact added")

def search_contact_entry():
    search_term = search_entry.get()
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

        contact_tracing_app_window = tk.Tk()
        contact_tracing_app_window.geometry("280x300")
        contact_tracing_app_window.title("COVID-19 Contact Tracing App") #title of GUI

        #widgets
        tk.Label(contact_tracing_app_window, text = "Name:", font = ("Helveltica", 10)).grid(row=0, column=0, sticky=tk.W)
        tk.Label(contact_tracing_app_window, text= "Phone Number:", font = ("Helveltica", 10)).grid(row=1, column=0, sticky=tk.W)
        tk.Label(contact_tracing_app_window, text= "Location visited:", font = ("Helveltica", 10)).grid(row=2, column=0, sticky=tk.W)
        tk.Label(contact_tracing_app_window, text= "Date visited:", font = ("Helveltica", 10)).grid(row=3, column=0, sticky=tk.W)

        global name_entry, number_entry, location_entry, date_entry, search_entry, result_text 

        name_entry = tk.Entry(contact_tracing_app_window)
        number_entry = tk.Entry(contact_tracing_app_window)
        location_entry = tk.Entry(contact_tracing_app_window)
        date_entry = tk.Entry(contact_tracing_app_window)

        name_entry.grid(row=0, column=1)
        number_entry.grid(row=1, column=1)
        location_entry.grid(row=2, column=1)
        date_entry.grid(row=3, column=1)

        button_1 = tk.Button(contact_tracing_app_window, text = "Add Contact", command = add_contact_entry)
        button_1.grid(row=4, column=0, columnspan=2, pady=5)

        tk.Label(contact_tracing_app_window, text = "Search Contact:", font = ("Helveltica", 10)).grid(row=5, column=0, sticky=tk.W)
        search_entry = tk.Entry(contact_tracing_app_window)
        search_entry.grid(row=5, column=1)
        button_2 = tk.Button(contact_tracing_app_window, text = "Search", command = search_contact_entry)
        button_2.grid(row=6, column=0, columnspan=2, pady=5)

        result_text = tk.Text(contact_tracing_app_window, height=10, width=40)
        result_text.grid(row=7, column=0, columnspan=2, pady=5)

        contact_tracing_app_window.mainloop()

if __name__ == "__main__":
    main()
