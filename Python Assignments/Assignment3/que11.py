#   age wise Ticket Cost Calculation with Discounts


ticket_price = float(input("Enter ticket price per person: "))
ages = []

for i in range(5):
    age = int(input(f"Enter age of person {i+1}: "))
    ages.append(age)

total_cost = 0

for age in ages:
    if age < 12:  
         total_cost += ticket_price * 0.7
    elif age > 59: 
        total_cost += ticket_price * 0.5
    else:  
        total_cost += ticket_price


print(f"Total ticket cost for 5 people: Rs. {total_cost:.2f}")

"""
Enter ticket price per person: 100
Enter age of person 1: 36
Enter age of person 2: 79
Enter age of person 3: 45
Enter age of person 4: 90
Enter age of person 5: 30
Total ticket cost for 5 people: Rs. 400.00  

"""