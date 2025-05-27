#Check if a given number is an Armstrong number

num = int(input("Enter a number: "))
sum = sum(int(digit) ** len(str(num)) 
          for digit in str(num))

if sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
