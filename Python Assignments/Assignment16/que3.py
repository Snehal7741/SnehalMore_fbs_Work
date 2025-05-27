class Shirt:
    # Static size-based price multipliers
    size_price_multiplier = {
        "small": 1.00,
        "medium": 1.10,
        "large": 1.20,
        "xlarge": 1.30
    }

    def __init__(self, sid=0, sname="Unknown", type="Casual", price=0.0, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.base_price = price  # original base price
        self.size = size.lower()
        self.adjust_price()  # adjust price based on size

    # Destructor
    def __del__(self):
        print("Destructor called for shirt: ",self.sname)

    # Method to adjust price based on size
    def adjust_price(self):
        multiplier = Shirt.size_price_multiplier.get(self.size, 1.0)
        self.price = self.base_price * multiplier

    # Method to display shirt details
    def show_book(self):
        print("Shirt ID:" ,self.sid)
        print("Shirt Name:" ,self.sname)
        print("Type: ",self.type)
        print("Size: ",self.size.capitalize())
        print("Price :", self.price)


# ---------- Testing the Shirt class ----------
if __name__ == "__main__":
    # Creating shirts with various sizes
    shirt1 = Shirt(201, "Formal White Shirt", "Formal", 1000, "small")
    shirt2 = Shirt(202, "Party Shirt", "Casual", 1000, "medium")
    shirt3 = Shirt(203, "Office Wear", "Formal", 1000, "large")
    shirt4 = Shirt(204, "Oversize Trend", "Casual", 1000, "xlarge")

    # Display details
    shirt1.show_book()
    shirt2.show_book()
    shirt3.show_book()
    shirt4.show_book()

'''
Shirt ID: 201
Shirt Name: Formal White Shirt
Type: Formal
Size: Small
Price : 1000.0
Shirt ID: 202
Shirt Name: Party Shirt
Type: Casual
Size: Medium
Price : 1100.0
Shirt ID: 203
Shirt Name: Office Wear
Type: Formal
Size: Large
Price : 1200.0
Shirt ID: 204
Shirt Name: Oversize Trend
Type: Casual
Size: Xlarge
Price : 1300.0
Destructor called for shirt: Formal White Shirt
Destructor called for shirt: Party Shirt
Destructor called for shirt: Office Wear
Destructor called for shirt: Oversize Trend

'''