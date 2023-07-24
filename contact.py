class Contact:
    #create constructor for contact info
    def __init__(self, name, number, location, date_of_visit):
        self.name = name
        self.number = number
        self.location = location
        self.date_of_visit = date_of_visit
    def __str__(self):
        return f'Name: {self.name}\nPhone Number: {self.number}\nLocation: {self.location}\nDate of Visit: {self.date_of_visit}'