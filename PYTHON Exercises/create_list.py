def show_cart(cart):
    if not isinstance(cart, list):
        return "Invalid cart"

    return f"Shopping Cart: {cart}"


cart = [100, 250, 75]

result = show_cart(cart)
print(result)