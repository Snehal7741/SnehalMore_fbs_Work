# to calculate the total ticket cost for passengers based on their age and the given discount conditions.

num_passengers = int(input("Enter the number of passengers: "))
ticket_cost = float(input("Enter per ticket cost: "))

total_cost = 0

for i in range(1, num_passengers + 1):
    age = int(input(f"Enter age of passenger {i}: "))

    if age < 12:
        discount = 0.30  
    elif age > 59:
        discount = 0.50  
    else:
        discount = 0  

    discounted_price = ticket_cost * (1 - discount)
    total_cost += discounted_price
    print(f"Passenger {i} Ticket Price: Rs. {discounted_price:.2f}")

print(f"\nTotal Ticket Cost for {num_passengers} passengers: Rs. {total_cost:.2f}")
