

amount = int(input("Enter the amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10]  # Currency denominations

print("Minimum number of notes needed:")
for note in notes:
    if amount >= note:
        count = amount // note
        amount %= note
        print("notes of ",note,"is:",count)


'''
notes of  200 is: 2
notes of  50 is: 1

'''