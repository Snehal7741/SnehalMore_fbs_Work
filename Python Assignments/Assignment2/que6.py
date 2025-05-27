#calculate total salary of emp based on basic,da=10% of basic ,ta=12%,hra=15% of basic

basic_salary = float(input("Enter the basic salary : "))


da = (10 / 100) * basic_salary  
ta = (12 / 100) * basic_salary  
hra = (15 / 100) * basic_salary 


total_salary = basic_salary + da + ta + hra

print(f"Total Salary of the employee is: {total_salary:.2f}")

'''
Enter the basic salary : 40000
Total Salary of the employee is: 54800.00

'''