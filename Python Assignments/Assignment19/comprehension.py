# 1. Find all of the numbers from 1–1000 that are divisible by 8
num = [i for i in range(1, 1001) if i % 8 == 0]
print("Numbers divisible by 8:", num)

# 2. Find all of the numbers from 1–1000 that have a 6 in them
have_6 = [x for x in range(1, 1001) if '6' in str(x)]
print("Numbers that have a 6:", have_6)

# 3. Count the number of spaces in a string (take input from user)
user_input = input("Enter a string to count spaces: ")
space_count = sum([1 for char in user_input if char == ' '])
print("Number of spaces:", space_count)

# 4. Remove all of the vowels in a string (take input from user)
sentence = input("Enter a string: ")
no_vowels = ''.join([char for char in sentence if char.lower() not in 'aeiou'])
print("String without vowels:", no_vowels)

# 5. Find all of the words in a string that are less than 5 letters (take input from user)
text = input("Enter a string: ")
short_words = [word for word in text.split() if len(word) < 5]
print("Words with less than 5 letters:", short_words)

# 6. Use a dictionary comprehension to count the length of each word in a sentence (take input from user)
sentence2 = input("Enter a sentence: ")
word_lengths = {word: len(word) for word in sentence2.split()}
print("Word lengths:", word_lengths)

# 7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit
result = [x for x in range(1, 1001) if any(x % d == 0 for d in range(1, 10))]
print("Numbers divisible by any single digit from 1–9:", result)
