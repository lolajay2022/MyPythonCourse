class Employee:
    # class variable shared by all instances
    employer = 'Acme, Inc.'

    def __init__(self, name):
        # instance variable unique to each instance
        self.name = name    
        self.addresses = []

    def add_address(self, address):
        self.address.append(address)

class Address:
     def __init__(self, type, street, city, state, zip):
        # instance variable unique to each instance
        self.type = type
        self.street = street
        self.city = city
        self.state = state    
        self.zip = zip

bob = Employee('Bob')
bob.add_address(Address('home','123 Mary Street','Pittsburgh','PA','15221'))
bob.add_address(Address('work','123 Mary Street','Pittsburgh','PA','15221'))

