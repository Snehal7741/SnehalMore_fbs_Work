
#Write a program to prompt user to enter userid and password. After verifying userid 
# and password display a 4 digit random number and ask user to enter the same.
#  If user enters the same number then show him success message otherwise  failed

import random

correct_userid = "admin"
correct_password = "12345"

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == correct_userid and password == correct_password:
    print("Login Successful!")

   
    random_number = random.randint(1000, 9999)
    print(f"Verification Code is : ",random_number)

    user_input = int(input("Enter the verification code: "))

    if user_input == random_number:
        print("you have verified succesfully.")
    else:
        print("Verification Failed! Incorrect Code.")
else:
    print("Invalid User ID or Password. Access Denied.")


''''
Enter User ID: admin
Enter Password: 12345
Login Successful!
Verification Code is :  8861
Enter the verification code: 8861
you have verified succesfully.

'''