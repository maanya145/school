#Writing multiple records.
import pickle

with open("students.dat", "wb") as file:
    for i in range(3):
        roll = int(input("Enter the roll no.: "))
        name = input("Enter the name: ")
        marks = float(input("Enter Marks: "))
        records = {"roll": roll, "name": name, "marks": marks}
        pickle.dump(records, file)

