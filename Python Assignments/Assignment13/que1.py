#1. Add a Key-Value Pair to the Dictionary
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3
print(my_dict)

#2. Concatenate Two Dictionaries Into One
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)

#3. Check if a Given Key Exists in a Dictionary or Not
my_dict = {'a': 1, 'b': 2}
key = 'a'
if key in my_dict:
    
  print("Key exists.")
else:
   
 print("Key does not exist.")

#4. Generate a Dictionary of (x, x*x*x) for 1 to n
n = 5
cube_dict = {x: x**3 for x in range(1, n+1)}
print(cube_dict)

#5. Sum All the Items in a Dictionary
my_dict = {'a': 10, 'b': 20, 'c': 30}
total = sum(my_dict.values())
print("Sum:", total)




#6. Multiply All the Items in a Dictionary
my_dict = {'a': 2, 'b': 3, 'c': 4}
result = 1
for value in my_dict.values():
   result *= value
print("Product:", result)

#7. Remove the Given Key from a Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'
if key_to_remove in my_dict:

  del my_dict[key_to_remove]
print(my_dict)

#8. Count Frequency of Words in a String Using Dictionary
text = "this is a test this is only a test"
word_freq = {}
for word in text.split():

    word_freq[word] = word_freq.get(word, 0) + 1
print(word_freq)
