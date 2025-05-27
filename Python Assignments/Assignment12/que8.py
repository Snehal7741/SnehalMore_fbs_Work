#que.8 Remove the characters of odd index values in a string

s1 ="Firstbit Solutions , data science fullstack"

s2 = ""

for i in range(len(s1)):
    if i % 2 == 0:
        s2 += s1[i]

print("even index of String:", s2)

#even index of String: Frti ouin  aasineflsak