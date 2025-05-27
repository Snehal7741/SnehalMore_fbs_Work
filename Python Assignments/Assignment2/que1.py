# Taking input from the user
hours = 2
minutes = 53
seconds = 50

# Converting to seconds using bitwise shift
total_seconds = (hours << 5) + (hours << 4) + (minutes << 6) + seconds  

print(f"Total seconds: {total_seconds}")
