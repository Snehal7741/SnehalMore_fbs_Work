def reverse_number(n, rev=0):
    if n == 0: 
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10) 


num = 6789  
reversed_num = reverse_number(num)
print("Reversed number:", reversed_num)

#Reversed number: 9876