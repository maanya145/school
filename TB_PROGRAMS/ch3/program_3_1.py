# Program 3.1
# Write a program to add two numbers using a function.

def calcSum(x, y):
    return x + y

# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calling the function
sum_result = calcSum(num1, num2)

# Displaying the result
print("Sum of two given numbers is", sum_result)
