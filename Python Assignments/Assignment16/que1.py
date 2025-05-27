class Book:
    # static variable to keep count of objects
    count = 0

    def __init__(self, bid=0, bname="Not Given", price=0.0, author="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1  # increment count when object is created

    def __del__(self):
        print(f"Book object with ID {self.bid} is destroyed")
        Book.count -= 1  # decrement count when object is destroyed

    def show_book(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

    @staticmethod
    def show_count():
        print("Total Book Objects Created:", Book.count)


# Testing the Book class
b1 = Book()
b1.show_book()
Book.show_count()

print()

b2 = Book(101, "Python Basics", 499.99, "John Doe")
b2.show_book()
Book.show_count()

'''
Book ID: 0
Book Name: Not Given
Price: 0.0
Author: Unknown
Total Book Objects Created: 1

Book ID: 101
Book Name: Python Basics
Price: 499.99
Author: John Doe
Total Book Objects Created: 2
Book object with ID 0 is destroyed
Book object with ID 101 is destroyed

'''