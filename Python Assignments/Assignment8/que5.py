#Sum of all prime numbers between 1 to n

#type 1 function w/o par w/o return
def sum_of_primes():
    n = 20  
    total = 0
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(1, n + 1):
        if is_prime(i):
            total += i

    print("Sum of prime numbers from 1 to", n, "is:", total)

sum_of_primes()

#type2 function w/o par  w return
def sum_of_primes():
    n = 20  
    total = 0

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(1, n + 1):
        if is_prime(i):
            total += i

    return total  

prime_sum = sum_of_primes()

print("Sum of prime numbers from 1 to 20 is:", prime_sum)


#type3 function w par  w/o return
def sum_of_primes(n):
    total = 0
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            total += num
    print("Sum of prime numbers from 1 to", n, "is:", total)
sum_of_primes(20)


#type4  w par  - w return

def sum_of_primes(n):
    total = 0

    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            total += num

    return total  

n = 20
prime_sum = sum_of_primes(n)

print("Sum of prime numbers from 1 to", n, "is:", prime_sum)
