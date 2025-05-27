#Program to Print Armstrong Numbers in a Given Range

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Armstrong numbers between {start} and {end} are:")

for num in range(start, end + 1):
    
    order = len(str(num)) 
    sum_of_powers = 0  
    while num > 0:
        digit = num % 10  
        sum += digit ** order  
        num //= 10  
    if sum == num:
        print(num, end=" ")
