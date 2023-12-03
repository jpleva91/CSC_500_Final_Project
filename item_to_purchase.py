class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.00
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.get_item_cost():.2f}')

    def get_item_cost(self):
        return self.item_price * self.item_quantity

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')

    def set_item_attributes(self, name=None, description=None, price=None, quantity=None):
        if name is not None:
            self.item_name = name
        else:
            self.item_name = input("Enter the item name: ")

        if description is not None:
            self.item_description = description
        else:
            self.item_description = input("Enter the item description: ")

        if price is not None:
            try:
                self.item_price = float(price)
            except ValueError:
                print("Invalid price. Please enter a valid number.")
        else:
            try:
                self.item_price = float(input("Enter the item price: "))
            except ValueError:
                print("Invalid price. Please enter a valid number.")

        if quantity is not None:
            try:
                self.item_quantity = int(quantity)
            except ValueError:
                print("Invalid quantity. Please enter a valid integer.")
        else:
            try:
                self.item_quantity = int(input("Enter the item quantity: "))
            except ValueError:
                print("Invalid quantity. Please enter a valid integer.")

    def set_item_quantity(self, quantity):
        try:
            self.item_quantity = int(quantity)
        except ValueError:
            print("Invalid quantity. Please enter a valid integer.")