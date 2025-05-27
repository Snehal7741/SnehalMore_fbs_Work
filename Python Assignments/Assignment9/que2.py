# 2. Check if a number is Armstrong using recursion
def armstrong(num, power, sum=0):
    if num == 0:
        return sum
    return armstrong(num // 10, power, sum + (num % 10) ** power)

num = 153  
if armstrong(num, len(str(num))) == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

#153 is an Armstrong number