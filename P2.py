#Write a program that reads a string and checks whether it is a palindrone string or not
# Read input from user
import datetime
current_time = datetime.datetime.today()
print(current_time)


string = input("Enter a string: ")

# Convert to lowercase and remove spaces
string = string.lower().replace(" ", "")

# Check if the string is equal to its reverse
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
