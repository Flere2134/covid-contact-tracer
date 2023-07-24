from contact import Contact
from file_handler import FileHandler

class ContactTracingApp:
    #constructor
    def __init__(self, filename = "contacts.txt"):
        self.filename = filename
    #add contact method
    def add_contact(self, name, number, location, date_of_visit):
        contact = Contact(name, number, location, date_of_visit)
        FileHandler.write_contact(contact, self.filename)
    #search contact method
    def search_contact(self, search_term):
        contacts = FileHandler.read_contact(self.filename)
        matching_contacts = []
        for contact in contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.number:
                matching_contacts.append(contact)
        return matching_contacts