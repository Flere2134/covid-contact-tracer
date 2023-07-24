from contact import Contact

class FileHandler:
    #method for writing/adding contact
    def write_contact(self, contact, filename):
        with open(filename, "a") as file:
            file.write(f'{contact.name}, {contact.number}, {contact.location}, {contact.date_of_visit}\n')
    #method for reading contact
    def read_contact(self, filename):
        contacts = []
        with open(filename, "r") as file:
            for line in file:
                name, number, location, date_of_visit = line.strip().split(',')
                contacts.append(Contact(name, number, location, date_of_visit))
        return contacts