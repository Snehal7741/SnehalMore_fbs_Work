# Custom exception for invalid TV data
class InvalidTelevisionData(Exception):
    def __init__(self, msg="Invalid input for television data."):
        self.msg = msg
        super().__init__(self.msg)

# Television class
class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def input_data(self):
        model_number = int(input("Enter model number (max 4 digits): "))
        screen_size = int(input("Enter screen size (in inches): "))
        price = int(input("Enter price (Rs): "))

        # Validation checks
        if model_number > 9999:
            raise InvalidTelevisionData("Model number must be 4 digits or less.")
        if screen_size < 12 or screen_size > 70:
            raise InvalidTelevisionData("Screen size must be between 12 and 70 inches.")
        if price < 0 or price > 5000:
            raise InvalidTelevisionData("Price must be between 0 and 5000 Rs.")

        # Set data if all inputs are valid
        self.model_number = model_number
        self.screen_size = screen_size
        self.price = price

    def display_data(self):
        print(f"\nTelevision Details:")
        print(f"Model Number: {self.model_number}")
        print(f"Screen Size : {self.screen_size} inches")
        print(f"Price       : ₹{self.price}")

# Main function
def main():
    tv = Television()
    try:
        tv.input_data()
    except (ValueError, InvalidTelevisionData) as e:
        print("Exception:", e)
        # Reset data to zero if exception is caught
        tv.model_number = 0
        tv.screen_size = 0
        tv.price = 0
    finally:
        tv.display_data()

# Run the program
main()
