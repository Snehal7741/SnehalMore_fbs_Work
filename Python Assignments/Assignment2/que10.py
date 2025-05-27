
# Write a program to reverse three digit number
num = int(input("Enter a three-digit number: "))

if num < 100 or num > 999:
    print("Please enter a valid three-digit number.")
else:
    rev_num = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)
    print(f"Reversed number: ",rev_num)
