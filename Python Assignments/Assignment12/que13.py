 #que13. Count number of digits and letters in a string

s1 ="FirstbiT  SolutionS 2015"
dig_count = 0
ch_count = 0

for ch in s1:
    if ch.isdigit():
        dig_count += 1
    elif ch.isalpha():
        ch_count += 1

print("Number of digits:", dig_count)
print("Number of letters:", ch_count)
'''
Number of digits: 4
Number of letters: 17
'''