from item_to_purchase import ItemToPurchase
from shopping_cart import ShoppingCart


# Print the menu
def print_menu(sc):
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit\n")
    user_input = input("Choose an option:\n")
    while user_input != "a" and user_input != "r" and user_input != "c" and user_input != "i" and user_input != "o" and user_input != "q":
        user_input = input("Choose an option:\n")
    if user_input == "o":
        sc.print_total()
    elif user_input == "i":
        sc.print_descriptions()
    elif user_input == "a":
        add_item_to_cart(sc)
    elif user_input == "r":
        remove_item_from_cart(sc)
    elif user_input == "c":
        change_item_quantity(sc)


def add_item_to_cart(sc):
    print("ADD ITEM TO CART\n")
    # Create a new item and add it to the cart
    item = ItemToPurchase()
    # Set the item attributes using item class method
    item.set_item_attributes()
    # Add the item to the cart
    sc.add_item(item)


def remove_item_from_cart(sc):
    print("REMOVE ITEM FROM CART\n")
    # Get the name of the item to remove
    item_name = input("Enter name of item to remove:\n")
    # Remove the item from the cart
    sc.remove_item(item_name)


def change_item_quantity(sc):
    print("CHANGE ITEM QUANTITY\n")
    item_name = input("Enter the item name:\n")
    quantity = input("Enter the new quantity:\n")
    # Create a new item with the name and quantity
    item = ItemToPurchase()
    item.item_name = item_name
    item.item_quantity = quantity
    # Modify the item in the cart
    sc.modify_item(item)


if __name__ == "__main__":
    # Get the customer name and date
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")

    # Initialize the shopping cart
    shopping_cart = ShoppingCart(customer_name, current_date)

    continue_shopping = True
    # Continue shopping until the user quits
    while continue_shopping:
        print_menu(shopping_cart)
        if input("Continue shopping? (y/n): ") == "n":
            continue_shopping = False

    print("Thank you for shopping with us!")
