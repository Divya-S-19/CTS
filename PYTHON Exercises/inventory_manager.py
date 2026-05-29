class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock


inventory = {
    "A": Product("Laptop", 5),
    "B": Product("Phone", 2)
}

low_stock = set()

for k, v in inventory.items():
    if v.stock < 3:
        low_stock.add(v.name)

print("Low Stock:", low_stock)