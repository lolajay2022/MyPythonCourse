class Item:
    def __init__(self):
        self.__price = 500

    def print_price(self):
        print("Price: {}".format(self.__price))

    def set_price(self, price):
        self.__price = price

c = Item()
c.print_price()

# try to change the price
c.__price = 888
c.print_price()

# using setter function
c.set_price(700)
c.print_price()

