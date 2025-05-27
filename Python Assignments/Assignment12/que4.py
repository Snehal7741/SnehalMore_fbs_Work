#Que4.Form a new string where first and last characters are exchanged

s1 = "FirstBit Solutions"

if len(s1) > 1:
    s1 = s1[-1] + s1[1:-1] + s1[0]
    print("Modified string:", s1)
else:
    print("String too short to swap.")

#Modified string: sirstBit SolutionF