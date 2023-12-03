# Define Shopping cart class

class ShoppingCart:
    customer_name = "none"
    current_date = "January 1, 2020"
    cart_items = []

    # Initialize the shopping cart taking in the customer name and current date
    def __init__(self, customer_name, current_date):
        if customer_name is not None:
            self.customer_name = customer_name
        if current_date is not None:
            self.current_date = current_date

    # Add an item to the cart
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    # Remove an item from the cart
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    # Modify an item in the cart
    def modify_item(self, ItemToPurchase):
        for item in self.cart_items:
            if item.item_name == ItemToPurchase.item_name:
                item.item_quantity = ItemToPurchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    # Get the number of items in the cart
    def get_num_items_in_cart(self):
        return sum(int(item.item_quantity) for item in self.cart_items)

    # Get the cost of the cart
    def get_cost_of_cart(self):
        return sum(item.get_item_cost() for item in self.cart_items)

    # Print the total cost of the cart
    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        for item in self.cart_items:
            item.print_item_cost()
        print(f"\nTotal: ${self.get_cost_of_cart():.2f}")

    # Print the descriptions of the items in the cart
    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        for item in self.cart_items:
            item.print_item_description()