class Shirt:
    def __init__(self, sid=0, sname="Not Given", type="Formal", price=0.0, size="Medium"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print(f"Shirt object with ID {self.sid} is destroyed")

    def show_shirt(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Price:", self.price)
        print("Size:", self.size)


# Creating default shirt (parameterless)
s1 = Shirt()
s1.show_shirt()

print()

# Creating parameterized shirt
s2 = Shirt(101, "Arrow Shirt", "Casual", 999.99, "Large")
s2.show_shirt()

'''
Shirt ID: 0
Shirt Name: Not Given
Type: Formal
Price: 0.0
Size: Medium

Shirt ID: 101
Shirt Name: Arrow Shirt
Type: Casual
Price: 999.99
Size: Large
Shirt object with ID 0 is destroyed
Shirt object with ID 101 is destroyed

'''