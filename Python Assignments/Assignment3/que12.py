# Check if a 3-Digit Number is a Palindrome


num = int(input("Enter a 3-digit number: "))

dig = num // 100         
que= (num // 10) % 10 
rev = num % 10    

if dig == rev:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

'''
Enter a 3-digit number: 121
121 is a palindrome.'

'''
