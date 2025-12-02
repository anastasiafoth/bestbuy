

class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name can´t be empty.")

        if price < 0:
            raise ValueError("Price can´t be negative.")

        if quantity < 0:
            raise ValueError("Quantity can´t be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity can´t be negative.")

        self.quantity = quantity

        #Deactivates product if quantity is zero
        if self.quantity == 0:
            self.active == False

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        if quantity < 0 or (self.quantity - quantity) < 0:
            raise ValueError("Quantity can´t be negative.")

        #updates quantity of the product
        self.quantity -= quantity

        return quantity * self.price

