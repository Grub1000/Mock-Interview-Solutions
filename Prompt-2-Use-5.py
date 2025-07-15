# 🧩 Problem: Inventory Management System
# You are helping a small business automate its inventory management. The business wants to track the products they have in stock and be able to:
# Add a new product.
# Update the quantity of a product.
# Remove a product.
# Get a sorted list of products by name.

# Each product has:
# A unique product_id (string)
# A name (string)
# A quantity (integer)

# 👉 Your Task:
# Implement a class called InventoryManager with the following methods:


class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product_id: str, name: str, quantity: int) -> bool:
        unique = True
        for i in range(len(self.products)):
            if self.products[i][0] == product_id:
                unique == False
        if unique:
            self.products.append([product_id, name, quantity])
            return(True)
        else:
            return(False)
        """Adds a product to the inventory.
        Returns True if successful, False if product_id already exists."""

    def update_quantity(self, product_id: str, quantity: int) -> bool:
        for i in range(len(self.products)):
            if self.products[i][0] == product_id:
                self.products[i][2] = quantity
                return(True)
        return(False)
        """Updates the quantity of the given product.
        Returns True if successful, False if product_id doesn't exist."""

    def remove_product(self, product_id: str) -> bool:
        deleteIndex = None
        for i in range(len(self.products)):
            if self.products[i][0] == product_id:
                deleteIndex = i
        return(self.products.pop(deleteIndex))
        """Removes the product from inventory.
        Returns True if successful, False if product_id doesn't exist."""

    def list_products(self) -> list[tuple[str, str, int]]:
        print(sorted(self.products, key=lambda i: i[1]))
        return(sorted(self.products, key=lambda i: i[1]))
        """Returns a list of all products as (product_id, name, quantity),
        sorted by product name in ascending order."""
    

inv = InventoryManager()
inv.add_product("p001", "Apple", 50)
inv.add_product("p002", "Banana", 30)
inv.update_quantity("p002", 45)
inv.remove_product("p001")
inv.list_products()

# Expected output: [("p002", "Banana", 45)]