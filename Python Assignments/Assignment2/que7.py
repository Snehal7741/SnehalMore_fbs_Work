#find the sum of 3 digit number

num = int(input("Enter a the number: "))


digit1 = num % 10  
num //= 10

digit2 = num % 10  
num //= 10

digit3 = num      


sum = digit1 + digit2 + digit3

# Output the result
print(f"Sum of the digits is: ",sum)

'''
Enter a the number: 234
Sum of the digits is:  9
7
'''