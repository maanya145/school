#Write a program to create a binary file with name and roll number> Search for a given roll number and display the name, if not found display appropriate message.
import pickle

with open("students.dat", "wb") as file:
    n = int(input("Enter the number of students: "))
    for i in range(n):
        name = input("Enter the name: ")
        roll_number = int(input("Enter the roll number: "))
        pickle.dump([name, roll_number], file)

with open("students.dat", "rb") as file:
    roll_number = int(input("Enter the roll number to search: "))
    found = False
    for i in range(n):
        record = pickle.load(file)
        if record[1] == roll_number:
            print("Record found")
            print(f"Name: {record[0]}, Roll Number: {record[1]}")
            found = True
            break
    if not found:
        print("Record not found")

