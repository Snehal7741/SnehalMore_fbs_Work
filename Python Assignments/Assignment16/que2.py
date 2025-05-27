class Product:
    # Static member
    discount = 0.0

    # Constructor (parameterized and parameterless)
    def __init__(self, pid=0, pname="Unknown", price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    # Destructor
    def __del__(self):
        print(f"Destructor called for product: {self.pname}")

    # Method to display product details
    def show_book(self):
        print(f"Product ID: {self.pid}")
        print(f"Product Name: {self.pname}")
        print(f"Price after discount: {self.price}")
        print(f"Quantity: {self.quantity}")

    # Method to apply discount
    def apply_discount(self):
        self.price = self.price - (self.price * Product.discount / 100)

    # Static method to set discount
    @staticmethod
    def set_discount(value):
        Product.discount = value


# ---------- Testing the Product class ----------
if __name__ == "__main__":
    # Set static discount for all products
    Product.set_discount(10)  # 10% discount

    # Create product objects
    p1 = Product(101, "Laptop", 50000, 3)
    p2 = Product()

    # Apply discount
    p1.apply_discount()

    # Show product details
    p1.show_book()
