import csv
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression

# Load data from CSV file
dates = []
numbers = []
with open("Thailand Lottary - Sheet1.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        # Convert date string to datetime object
        date = datetime.strptime(row[0], "%d/%m/%y")
        # Convert number string to integer
        if row[1]:
            numbers.append(int(row[1]))
        else:
            numbers.append(None)  # If no number, set it as None
        dates.append([date.day, date.month, date.year])

# Convert lists to numpy arrays
X = np.array(dates)
y = np.array(numbers)

# Filter out rows with missing numbers
X = X[y != None]
y = y[y != None]

# Initialize and fit linear regression model
model = LinearRegression().fit(X, y)

# Predict the next date
last_date = datetime.strptime(row[0], "%d/%m/%y")
if last_date.day == 16:
    if last_date.month == 12:
        next_date = datetime(last_date.year + 1, 1, 1)
    else:
        next_date = datetime(last_date.year, last_date.month + 1, 1)
else:
    next_date = datetime(last_date.year, last_date.month, 16)

# Predict the next number
next_number = model.predict([[next_date.day, next_date.month, next_date.year]])

# Ensure the next number is a 3-digit integer within range [100, 999]
next_number = max(100, min(999, int(round(next_number[0]))))

# Display the prediction
print("Next date:", next_date.strftime("%d/%m/%y"))
print("Predicted next number:", next_number)

# Prompt the user to input the actual number
actual_number = input("Enter the actual number: ")

# Write the next date, predicted number, and actual number to CSV file
with open("Thailand Lottary - Sheet1.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow([next_date.strftime("%d/%m/%y"), str(next_number), actual_number])  # Writing the next date, predicted number, and actual number
