class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False
