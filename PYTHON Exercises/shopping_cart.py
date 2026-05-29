class CartItem:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def total(self):
        return self.price * self.qty


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.total() for item in self.items)

    def print_receipt(self):
        total = self.calculate_total()
        gst = total * 0.18
        final = total + gst

        print("\n--- Receipt ---")
        for item in self.items:
            print(item.name, item.total())

        print("Subtotal:", total)
        print("GST (18%):", gst)
        print("Total:", final)


cart = ShoppingCart()
cart.add_item(CartItem("Book", 100, 2))
cart.add_item(CartItem("Pen", 10, 5))
cart.print_receipt()