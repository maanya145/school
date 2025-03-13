#1. Write a Python program to find the LCM (Least Common Multiple) of two numbers 
#.
# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Start from the maximum of the two numbers
max_num = max(num1, num2)

# Keep increasing max_num until it is divisible by both numbers
while True:
    if max_num % num1 == 0 and max_num % num2 == 0:
        lcm = max_num
        break
    max_num += 1  # Increment by 1 until LCM is found

# Displaying the result
print(f"The LCM of {num1} and {num2} is {lcm}")



#2.Write a Python program to reverse a given number without converting it to a string.
# Taking input from the user
num = int(input("Enter a number: "))

# Initialize reversed number
#0to 0
rev_num = 0

# Reverse the number using a loop
while num > 0:
    digit = num % 10  # Extract the last digit
    rev_num = rev_num * 10 + digit  # Append the digit
    num //= 10  # Remove the last digit from num

# Display the reversed number
print("Reversed Number:", rev_num)



# 3. Write a Python program to count the frequency of elements in a list without using the count() method.
# Taking input: list of elements
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 3, 2]

# Creating an empty dictionary to store frequency
frequency = {}

# Iterating through the list
for num in numbers:
    if num in frequency:
        frequency[num] += 1  # Increment count if already in dictionary
    else:
        frequency[num] = 1  # Initialize count if not in dictionary

# Displaying the frequency of elements
print("Element Frequency Count:")
for key, value in frequency.items():
    print(f"{key}: {value}")


#4.Write a Python program to count the occurrences of each vowel in a given string without using a function.
#Taking input from the user
string = input("Enter a string: ").lower()  # Convert to lowercase for case insensitivity

# Vowel dictionary to store counts
vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Iterate through each character in the string
for char in string:
    if char in vowel_count:  # Check if the character is a vowel
        vowel_count[char] += 1  # Increment the count

# Display the vowel occurrences
print("Vowel occurrences:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")
