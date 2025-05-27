#Write a program to check if person is eligible to marry or not (male age >=21 and female age=>18


gender = input("Enter your gender (male/female): ").strip().lower()
age = int(input("Enter your age: "))

if (gender == "male" and age >= 21) or (gender == "female" and age >= 18):
    
    print("You are eligible for marriage.")
else:
    print("You are NOT eligible for marriage.")


'''
 Enter your gender (male/female): female
Enter your age: 20
You are eligible for marriage.
   ''' 
