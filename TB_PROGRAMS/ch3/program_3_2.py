# Program 3.2
# Write a program to calculate simple interest using a function.
# The function should accept principal amount, time, and rate, and return the calculated interest.
# Use default values of 2 years for time and 10% for rate.

def interest(principal, time=2, rate=0.10):
    return principal * rate * time

# Main program
prin = float(input("Enter principal amount: "))

# Using default time and rate values
print("Simple interest with default ROI and time values is:")
si1 = interest(prin)
print("Rs.", si1)

# Taking user input for rate and time
roi = float(input("Enter rate of interest (ROI): "))
time = int(input("Enter time in years: "))

# Using user-provided values
print("Simple interest with your provided ROI and time values is:")
si2 = interest(prin, time, roi / 100)
print("Rs.", si2)
