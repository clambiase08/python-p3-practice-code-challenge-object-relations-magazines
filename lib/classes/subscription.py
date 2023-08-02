from classes.reader import Reader
from classes.magazine import Magazine


class Subscription:
    all = []

    def __init__(self, magazine, reader, price):
        self.magazine = magazine
        self.reader = reader
        self.price = price
        Subscription.all.append(self)

    @property
    def reader(self):
        return self._reader

    @reader.setter
    def reader(self, reader):
        if isinstance(reader, Reader):
            self._reader = reader
        else:
            raise Exception("reader must be a Reader instance")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception("magazine must be a Magazine instance")

    @property
    def price(self):
        return float("{:.2f}".format(self._price))

    @price.setter
    def price(self, price):
        if type(price) == float and 1.00 <= price <= 49.99:
            self._price = price
        else:
            raise Exception("Invalid price")

    def print_details(self):
        print(f"{self.reader} subscribed to {self.magazine} for ${self.price}")

    # def __repr__(self):
    #     return f"<Subscription | Magazine: {self.magazine}, Reader: {self.reader}, Price: {self.price}>"
