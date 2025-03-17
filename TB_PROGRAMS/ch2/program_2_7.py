# Program 2.7
# Modify Program 2.6 to ignore case differences while matching values.

info = {'Riya': 'CSc.', 'Mark': 'Eco', 'Ishpreet': 'Eng', 'Kamaal': 'Env.Sc'}

inp = input("Enter value to be searched for: ")

for a in info:
    if info[a].upper() == inp.upper():
        print("The key of given value is", a)
        break
else:
    print("Given value does not exist in dictionary")
