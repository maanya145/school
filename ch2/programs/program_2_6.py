# Program 2.6
# Write a program that checks for the presence of a value inside a dictionary and prints its key.

info = {'Riya': 'CSc.', 'Mark': 'Eco', 'Ishpreet': 'Eng', 'Kamaal': 'Env.Sc'}

inp = input("Enter value to be searched for: ")

if inp in info.values():
    for a in info:
        if info[a] == inp:
            print("The key of given value is", a)
            break
else:
    print("Given value does not exist in dictionary")
