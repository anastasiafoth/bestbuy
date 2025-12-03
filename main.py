import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def show_products() -> list:
    """Display all available products in the store."""
    list_of_products = best_buy.get_all_products()
    for i, product in enumerate(list_of_products):
        print(f"{i+1}. ",end=""), product.show()
    return list_of_products


def make_order():
    order_list = []
    print("------")
    list_of_products = show_products()
    print("------")
    print("When you want to finish order, enter empty text.")

    while True:
        product_index = input("Which product # do you want? ")
        if product_index == "":
            break
        if not product_index.isdigit():
            print("Please enter a number!")

        # - 1 so we have the correct index for the list
        product_index = int(product_index) - 1
        quantity = int(input("What amount do you want? "))

        order_list.append((list_of_products[product_index], quantity))
        print("Product added to list!")
        print()

    #ordering
    price_total = best_buy.order(order_list)
    print("********")
    print(f"Order made! Total payment: ${price_total}")


def start() -> None:
    """Display the main menu of the store application."""

    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Make an order\n"
          "4. Quit")


def main() -> None:
    """Main function to run the store application.
    
    This function handles the main loop of the application, presenting the menu
    and processing user input to interact with the store's functionality.
    """
    while True:
        start()
        user_input_menu = input("Please choose a number: ")

        if not user_input_menu.isdigit():
            print("Please enter a number!")
            continue
        user_input_menu = int(user_input_menu)

        if not (1 <= user_input_menu <= 4):
            print("Please enter a number between 1 and 4.")
            continue

        if user_input_menu == 1:
            show_products()

        elif user_input_menu == 2:
            total_quantity = best_buy.get_total_quantity()
            print(f"Total of {total_quantity} items in store")

        elif user_input_menu == 3:
            make_order()

        elif user_input_menu == 4:
            print("Bye!")
            break

if __name__ == "__main__":
    main()
