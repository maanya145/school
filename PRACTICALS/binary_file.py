# 1. Write and Read Data from Binary File
import pickle

# Writing to binary file
data = {'roll': 101, 'name': 'Arjun', 'marks': 95}

with open('student.dat', 'wb') as file:
    pickle.dump(data, file)

# Reading from binary file
with open('student.dat', 'rb') as file:
    student = pickle.load(file)
    print(student)

import pickle

# 2. Writing multiple records
with open('students.dat', 'wb') as file:
    for i in range(3):
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        record = {'roll': roll, 'name': name, 'marks': marks}
        pickle.dump(record, file)

# Reading all records
with open('students.dat', 'rb') as file:
    try:
        while True:
            record = pickle.load(file)
            print(record)
    except EOFError:
        pass

#  3. Search a Record by Roll Number
import pickle

roll_search = int(input("Enter Roll No to Search: "))
found = False

with open('students.dat', 'rb') as file:
    try:
        while True:
            record = pickle.load(file)
            if record['roll'] == roll_search:
                print("Record Found:", record)
                found = True
                break
    except EOFError:
        if not found:
            print("Record not found")
#4.Update a Record in Binary File
import pickle
updated_records = []
roll_update = int(input("Enter Roll No to Update: "))

with open('students.dat', 'rb') as file:
    try:
        while True:
            record = pickle.load(file)
            if record['roll'] == roll_update:
                record['name'] = input("Enter New Name: ")
                record['marks'] = float(input("Enter New Marks: "))
            updated_records.append(record)
    except EOFError:
        pass

with open('students.dat', 'wb') as file:
    for record in updated_records:
        pickle.dump(record, file)

print("Record Updated Successfully.")

#5. Delete a Record from Binary File
import pickle

roll_delete = int(input("Enter Roll No to Delete: "))
records = []

with open('students.dat', 'rb') as file:
    try:
        while True:
            record = pickle.load(file)
            if record['roll'] != roll_delete:
                records.append(record)
    except EOFError:
        pass

with open('students.dat', 'wb') as file:
    for record in records:
        pickle.dump(record, file)

print("Record Deleted Successfully.")

# 6. Count Records in a Binary File
import pickle
count = 0
with open('students.dat', 'rb') as file:
    try:
        while True:
            pickle.load(file)
            count += 1
    except EOFError:
        pass
print("Total number of records:", count)

#7. Display Records with Marks Greater Than 90
import pickle

with open('students.dat', 'rb') as file:
    print("Students with Marks > 90:")
    try:
        while True:
            record = pickle.load(file)
            if record['marks'] > 90:
                print(record)
    except EOFError:
        pass