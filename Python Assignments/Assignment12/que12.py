#que 12. Count number of lowercase characters in a string

s1 ="FirstbiT  SolutionS "

lowc_count = 0

for ch in s1:
    if ch.islower():
        lowc_count += 1

print("Number of lowercase characters:", lowc_count)

#Number of lowercase characters: 13