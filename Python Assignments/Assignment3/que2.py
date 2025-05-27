#write a program to input any alphabet and check it vowels or consonants 


ch = input("Enter an alphabet: ").lower() 

if len(ch) == 1 and ch.isalpha():

    if ch in "aeiou":
        print(f"{ch} is a Vowel.")
    else:
        print(f"{ch} is a Consonant.")
else:
    print("Invalid input! Please enter a single alphabet.")

""""
Enter an alphabet: r
r is a Consonant.
"""

