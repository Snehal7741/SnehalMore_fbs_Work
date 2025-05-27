


feet = 5
inches = 10


total_inches = (feet * 12) + inches 
total_cm = total_inches * 2.54 

meters = int(total_cm // 100) 
centimeters = total_cm % 100

print(f"Distance: {meters} meters and {centimeters:.2f} centimeters")
