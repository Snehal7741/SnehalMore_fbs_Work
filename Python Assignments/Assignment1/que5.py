# WAP TO ENTER P,T,R AND CALCULATE SIMPLE INTEREST

P=20000
R=5
T=5
n=2

A = P * (1 + R / 100) ** (n * T)
CI = A - P  # Compound Interest

print("Final Amount is", round(A, 2))
print("Compound Interest is", round(CI, 2))

#Final Amount is 32577.89
#Compound Interest is 12577.89