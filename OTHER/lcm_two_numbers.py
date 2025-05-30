# 1. Write a Python program to find the LCM (Least Common Multiple) of two numbers

# date and time
import datetime

current_date = datetime.date.today()
print(current_date)

# Taking input from the user (simple enuf)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Start from the maximum of the two numbers (Take max)
max_num = max(num1, num2)

# Keep increasing max_num until it is divisible by both numbers
while True:
    if max_num % num1 == 0 and max_num % num2 == 0:
        lcm = max_num
        break
    max_num += 1  # Increment by 1 until LCM is found

# Displaying the result
print(f"The LCM of {num1} and {num2} is {lcm}")
