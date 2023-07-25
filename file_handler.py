from contact import Contact

class FileHandler:
    #method for writing/adding contact
    def write_contact(self, contact, file_name):
        with open(file_name, "a") as file:
            file.write(f'{contact.name}, {contact.number}, {contact.location}, {contact.date_of_visit}\n')
    #method for reading contact
    def read_contact(self, file_name):
        contacts = []
        with open(file_name, "r") as file:
            for line in file:
                name, number, location, date_of_visit = line.strip().split(',')
                contacts.append(Contact(name, number, location, date_of_visit))
        return contacts