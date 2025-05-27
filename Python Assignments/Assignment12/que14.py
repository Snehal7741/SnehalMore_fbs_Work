#que14. Count the occurrences of each word in a string

s1 = "We few, we happy few, we band of brothers"

words = s1.split()
word_occ= {}

for word in words:
    if word in word_occ:
        word_occ[word] += 1
    else:
        word_occ[word] = 1

print("Word occurrences:")
for word, count in word_occ.items():
    print(f"{word}: {count}")
'''
Word occurrences:
We: 1
few,: 2
we: 2
happy: 1
band: 1
of: 1
brothers: 1
'''