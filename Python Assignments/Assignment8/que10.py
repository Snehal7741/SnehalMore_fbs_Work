#Write a program to check if entered year is a leap year or not.

#Type-1: Without Parameter, Without Return
def check_leap_year():
    year = 2024 
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
check_leap_year()


#Type-2: Without Parameter, With Return
def check_leap_year():
    year = 2024 
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

result = check_leap_year()
print("Is leap year:", result)


#Type-3: With Parameter, Without Return
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

check_leap_year(2024)


#Type-4: With Parameter, With Return
def check_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = 2024
result = check_leap_year(year)

print(year, "is a leap year" if result else "is not a leap year")