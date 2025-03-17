# Program 2.2
# Write a program to create a dictionary containing names of competition 
# winner students as keys and number of their wins as values.

n = int(input("How many students? "))
CompWinners = {}

for a in range(n):
    key = input("Name of the student: ")
    value = int(input("Number of competitions won: "))
    CompWinners[key] = value

print("The dictionary now is:")
print(CompWinners)
