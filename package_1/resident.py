class Residence:
    def __init__(self, city, country, state, street, postal_code):
        self.city = city
        self.country = country
        self.state = state
        self.street = street
        self.postal_code = postal_code

    def display_residence(self):
        return f"City: {self.city}, Country: {self.country}, State: {self.state}, Street: {self.street}, Postal Code: {self.postal_code}"
