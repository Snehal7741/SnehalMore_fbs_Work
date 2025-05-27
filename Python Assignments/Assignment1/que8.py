# WAP TO CONVERT DAYS INTO YEARS MONTHS  AND DAYS

# Input total number of days
days = int(input("Enter total number of days: "))

years = days // 365
remaining_days = days % 365
months = remaining_days // 30
days = remaining_days % 30


print(years ,"Years : ", months , "Months : ", days, "Days : ")

"""
OUTPUT
Enter total number of days: 950
2 Years :  7 Months :  10 Days : 

"""