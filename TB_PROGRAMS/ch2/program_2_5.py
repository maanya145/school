# Program 2.5
# Write a program that finds an element’s index/position in a tuple WITHOUT using index().

tuple1 = ('a', 'p', 'p', 'l', 'e')

char = input("Enter a single letter without quotes: ")

if char in tuple1:
    count = 0
    for a in tuple1:
        if a != char:
            count += 1
        else:
            break
    print(char, "is at index", count, "in", tuple1)
else:
    print(char, "is NOT in", tuple1)
