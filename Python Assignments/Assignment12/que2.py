
#que2. Remove the nth index character from a non-empty string

s1 = "firstbit Solutions"
n = int(input("Enter the index to remove: "))

if 0 <= n < len(s1):
    new_str = s1[:n] + s1[n+1:]
    print("Modified string:", new_str)
else:
    print("Invalid index.")

#Enter the index to remove: 3
#Modified string: firtbit Solutions