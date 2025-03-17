# Program 3.3
# Write a program that receives two numbers in a function and returns the results 
# of all arithmetic operations (+, -, *, /, %).

def arCalc(x, y):
    return x + y, x - y, x * y, x / y, x % y

# Main program
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

# Calling the function and unpacking results
add, sub, mult, div, mod = arCalc(num1, num2)

# Displaying results
print("Sum of given numbers:", add)
print("Subtraction of given numbers:", sub)
print("Product of given numbers:", mult)
print("Division of given numbers:", div)
print("Modulo of given numbers:", mod)
