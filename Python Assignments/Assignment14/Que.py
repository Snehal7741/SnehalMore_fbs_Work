#1. Find elements in a set that are not in another set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
result = set1 - set2
print("Difference is :", result)
#Difference is : {1, 2, 3}

#2. Remove the intersection of a second set from a first set
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6}
set1 -= set1.intersection(set2)
print(" intersection with set2:", set1)
# intersection with set2: {1, 2, 5}

#3. Find all unique words and count frequency from a list
words = ["apple", "banana", "apple", "orange", "banana", "grape"]
word_set = set(words)
word_count = {word: words.count(word) for word in word_set}
print("Unique words and their frequency:", word_count)
#Unique words and their frequency: {'grape': 1, 'banana': 2, 'orange': 1, 'apple': 2}

#4. Find all pairs whose sum equals a given value
numbers = [2, 4, 3, 5, 7, 8, 1]
target_sum = 8
pairs = set()
for i in range(len(numbers)):
 for j in range(i+1, len(numbers)):
    if numbers[i] + numbers[j] == target_sum:
      pairs.add((numbers[i], numbers[j]))
print("Pairs with sum", target_sum, ":", pairs)
#Pairs with sum 8 : {(7, 1), (3, 5)}

#5. Find the longest common prefix using set (without function)
strings = ["flower", "flow", "flight"]

if strings:
    shortest = min(strings, key=len)
    prefix = ""
    for i in range(len(shortest)):
        char_set = set()
        for word in strings:
            char_set.add(word[i])
        if len(char_set) == 1:
            prefix += shortest[i]
        else:
            break
    print("Longest common prefix:", prefix)
else:
    print("No strings provided.")
#Longest common prefix: fl


# 6. Find two numbers whose product is maximum
numbers = [1, 20, 5, 4, 8, 10]
max_product = float('-inf')
pair = ()
for i in range(len(numbers)):
 for j in range(i+1, len(numbers)):
   product = numbers[i] * numbers[j]
 if product > max_product:
    max_product = product
 pair = (numbers[i], numbers[j])
print("Pair with maximum product:", pair)
#Pair with maximum product: (10, 10)

#7. Find missing numbers between two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1
print("Missing in set2:", missing_in_set2)
print("Missing in set1:", missing_in_set1)
#Missing in set2: {1, 2, 3}
#Missing in set1: {6, 7}

#8. Group anagrams together
from collections import defaultdict
words = ["bat", "tab", "tap", "pat", "cat", "act"]
anagrams = defaultdict(list)
for word in words:
 sorted_word = ''.join(sorted(word))
 anagrams[sorted_word].append(word)
print("Anagrams grouped together:", list(anagrams.values()))
#Anagrams grouped together: [['bat', 'tab'], ['tap', 'pat'], ['cat', 'act']]

#9. Find unique combinations of 3 numbers adding up to target
from itertools import combinations
numbers = [1, 2, 3, 4, 5, 6]
target = 9
combs = set()
for triplet in combinations(numbers, 3):
 if sum(triplet) == target:
   combs.add(tuple(sorted(triplet)))
print("Combinations of 3 numbers with sum", target, ":", combs)
#Combinations of 3 numbers with sum 9 : {(1, 2, 6), (2, 3, 4), (1, 3, 5)}