#que10 Take two strings and display the larger string without using built-in functions

s1 ="Firstbit Solutions data science fullstack"

s2="Firstbit Solutions data science"

len1 = len(s1)
len2 = len(s2)

if len1 > len2:
    print("Larger string is:", s1)
elif len2 > len1:
    print("Larger string is:", s2)
else:
    print("Both strings are equal in length.")

 #Larger string is: Firstbit Solutions data science fullstack