import csv
from datetime import datetime
import random

# Initialize an empty list to store data
data = []

# Read data from CSV file
with open("Thailand Lottary - Sheet1.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row
    print("Header:", header)  # Print the header row
    for row in reader:
        # Convert date string to datetime object
        date = datetime.strptime(row[0], "%d/%m/%y")  # Adjust the format string
        # Convert number string to integer
        if row[1]:  # Check if there's a number in the row
            number = int(row[1])
        else:
            number = None  # If no number, set it as None
        # Store in list
        data.append((date, number))

# Sort the dates
sorted_dates = sorted(data, key=lambda x: x[0])

# Find the next date
last_date = sorted_dates[-1][0]
if last_date.day == 16:  # If the last date is the 16th of the month
    if last_date.month == 12:  # If the last date's month is December
        next_date = datetime(last_date.year + 1, 1, 1)  # Next date is the 1st of January of the next year
    else:
        next_date = datetime(last_date.year, last_date.month + 1, 1)  # Next date is the 1st of the next month
else:
    next_date = datetime(last_date.year, last_date.month, 16)  # Next date is the 16th of the current month

# Print the next date
print("Next date:", next_date.strftime("%d/%m/%y"))

# Calculate the differences between consecutive numbers
differences = [sorted_dates[i+1][1] - sorted_dates[i][1] for i in range(len(sorted_dates)-1)]

# Calculate the average difference
average_difference = sum(differences) / len(differences)

# Estimate the next number with a smaller randomness
last_number = sorted_dates[-1][1]
next_number = last_number + average_difference + random.randint(-20, 20)  # Add a smaller random offset

# Ensure the next number is a 3-digit integer within range [100, 999]
next_number = max(100, min(999, round(next_number)))

print("Next number (estimated):", int(next_number))

# Write the next date and number to CSV file
with open("Thailand Lottary - Sheet1.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow([next_date.strftime("%d/%m/%y"), "{:03d}".format(int(next_number))])  # Writing the next date and 3-digit number
