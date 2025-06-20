# Write and read the data from binary file
import pickle


dat = {"roll": 101, "name": "Arjun", "marks": 95}
with open("student.dat", "wb") as file:
    pickle.dump(dat, file)
file.close()

# writing multiple records

with open("students.dat", "wb") as file:
    for i in range(3):
        roll = int(input("Enter the roll no"))
        name = input("Enter the name")
        marks = float(input("Enter the marks"))
        records = {"roll": roll, "name": name, "marks": marks}
        pickle.dump(records, file)

# Reading all records

with open("students.dat", "rb") as file:
    try:
        while True:
            record = pickle.load(file)
            print(record)
    except EOFError:
        pass

# Search the record by roll number

roll_search = int(input("Enter the roll number to search: "))
print("Record updated successfully")

# Update the record in binary file
updated_record = []
roll_update = int(input("Enter the roll number to update: "))
with open("students.dat", "rb") as file:
    try:
        while True:
            record = pickle.load(file)
            if record["roll"] == roll_update:
                record["name"] = input("Enter the new name: ")
                record["marks"] = int(input("Enter the new marks: "))
            updated_record.append(record)
    except EOFError:
        pass
with open("students.dat", "wb") as file:
    for record in updated_record:
        pickle.dump(record, file)

# delete record from the file

roll_delete = int(input("Enter the roll no. to be deleted "))

records = []

with open("students.dat", "rb") as file:
    try:
        while True:
            record = pickle.load(file)
            if record["roll"] != roll_delete:
                records.append(record)
    except EOFError:
        pass

with open("students.dat", "wb") as file:
    for record in records:
        pickle.dump(record, file)
print("Record deleted succesfully")


