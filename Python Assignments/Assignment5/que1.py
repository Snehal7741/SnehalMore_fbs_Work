#Python program to prompt the user to enter their user ID and password.
#  The user gets three attempts to enter the correct credentials


correct_userid = "admin"
correct_password = "password123"

attempts = 3

while attempts > 0:
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_userid and password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts -= 1
        print(f"Incorrect credentials! You have {attempts} attempt(s) left.")

if attempts == 0:
    print("Too many failed attempts. Program terminated.")
