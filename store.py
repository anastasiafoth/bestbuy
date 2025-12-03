class Store:

    def __init__(self, products):
        if type(products) == list:
            self.products = products


    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product not in self.products:
            raise ValueError("Product not in stock.")

        self.products.remove(product)

    def get_total_quantity(self) -> int:
        sum_quantity = 0
        for product in self.products:
            sum_quantity += product.quantity

        return sum_quantity

    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.active:
                active_products.append(product)

        return active_products

    def order(self, shopping_list) -> float:
        total_price = 0
        for product_to_order, quantity in shopping_list:
            product_to_order.buy(quantity)
            price_per_product = product_to_order.price * quantity
            total_price += price_per_product
        return total_price