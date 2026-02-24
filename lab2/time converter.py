# Take input from user
seconds = int(input("Enter time in seconds: "))

# Convert
hours = seconds // 3600
remaining_seconds = seconds % 3600
minutes = remaining_seconds // 60
secs = remaining_seconds % 60

# Output
print("Time is:")
print(hours, "hours", minutes, "minutes", secs, "seconds")
