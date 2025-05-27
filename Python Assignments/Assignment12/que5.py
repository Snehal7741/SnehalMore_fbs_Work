#que5. Count the number of vowels in a string

s1 = "FirstBit Solutions academy"

vowels = "aeiouAEIOU"
count = 0

for ch in s1:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)
#Number of vowels: 9