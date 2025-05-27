class Product:
    def __init__(self, pid=0, pname="Not Given", price=0.0, quantity="Unknown"):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
    

    def __del__(self):
        print(f"project object with ID {self.pid} is destroyed")

    def show_book(self):
        print("Product ID:", self.pid)
        print("product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity :", self.quantity)


# --- Testing ---

# Using parameterless constructor
p1= Product()
p1.show_book()

print("\n")

# Using parameterized constructor
p2 = Product(200, "Iphone 16", 122499.50, 3)
p2.show_book()

'''
Product ID: 0  
product Name: Not Given  
Price: 0.0  
Quantity : Unknown  

Product ID: 200  
product Name: Iphone 16  
Price: 122499.5  
Quantity : 3  

project object with ID 0 is destroyed  
project object with ID 200 is destroyed  

'''