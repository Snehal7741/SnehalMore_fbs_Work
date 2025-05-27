#que9 Calculate number of words and number of characters in a string

s1 ="Firstbit Solutions data science fullstack"

words = s1.split()
word_count = len(words)


ch_count = 0
for ch in s1:
    if ch.isalpha():
        ch_count += 1

print("Number of words:", word_count)
print("Number of characters :", ch_count)

'''
Number of words: 5
Number of characters : 37
'''