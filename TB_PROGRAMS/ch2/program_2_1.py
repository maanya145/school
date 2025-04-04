# Program 2.1
# Write a program that reads a line and prints its statistics like:
# - Number of uppercase letters
# - Number of lowercase letters
# - Number of alphabets
# - Number of digits

line = input("Enter a line :")

lowercount = uppercount = 0
digitcount = alphacount = 0

for a in line:
    if a.islower():
        lowercount += 1
    elif a.isupper():
        uppercount += 1
    elif a.isdigit():
        digitcount += 1

    if a.isalpha():
        alphacount += 1

print("Number of uppercase letters :", uppercount)
print("Number of lowercase letters :", lowercount)
print("Number of alphabets :", alphacount)
print("Number of digits :", digitcount)
