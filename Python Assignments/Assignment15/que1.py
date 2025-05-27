class Book:
    def __init__(self, bid=0, bname="Not Given", price=0.0, author="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
    

    def __del__(self):
        print(f"Book object with ID {self.bid} is destroyed")

    def show_book(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)


# --- Testing ---

# Using parameterless constructor
book1 = Book()
book1.show_book()

print("\n")

# Using parameterized constructor
book2 = Book(101, "Python Basics", 499.50, "John Doe")
book2.show_book()


'''
Book ID: 0
Book Name: Not Given
Price: 0.0
Author: Unknown

Book ID: 101
Book Name: Python Basics
Price: 499.5
Author: John Doe
Book object with ID 0 is destroyed
Book object with ID 101 is destroyed
'''