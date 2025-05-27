#Write a program to calculate profit or loss.

cost_price = float(input("Enter Cost Price : "))
selling_price = float(input("Enter Selling Price : "))


if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit is : ",profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print(f"Loss is :",loss)
else:
    print("No Profit, No Loss.")

    
'''
Enter Cost Price : 789
Enter Selling Price : 950
Profit is :  161.0
'''