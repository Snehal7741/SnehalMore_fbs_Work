# CALCULATE THE SELLING PRICE OF BOOK BASED ON COST PRICE AND DISCOUNT

cost_price = float(input("Enter the cost price of the book: "))
discount = float(input("Enter the discount percentage: "))

discount_amount = (discount / 100) * cost_price
selling_price = cost_price - discount_amount


print(f"Selling Price of the book is:",selling_price)


'''
Enter the cost price of the book: 270
Enter the discount percentage: 5
Selling Price of the book is: 256.5

'''