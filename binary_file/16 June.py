"""#Write and read the data from binary file

import pickle

dat={"roll":101,"name":"Arjun","marks":95}

with open ("student.dat","wb") as file:
    pickle.dump(dat,file)
file.close()

#writing multiple records

import pickle
with open("students.dat","wb") as file:
    for i in range(3):
        roll=int(input("Enter the roll no"))
        name=input("enter the name")
        marks=float(input("enter the marks"))
        records={"roll":roll,"name":name,"marks":marks}
        pickle.dump(records,file)

#Reading all records

with open("students.dat","rb") as file:
    try:
         while True:
             record=pickle.load(file)
             print(record)
    except EOFError:
        pass"""

"""#search the record by roll no.
import pickle
roll_search=int(input("Enter the roll no. to search"))
found=False
with open ("student.dat","rb") as file:
    try:
        while True:
            record=pickle.load(file)
            if record['roll']==roll_search:
                print("record Found",record)
                found=True
                break
    except EOFError:
        if not found:
            print("Record not Found")"""
'''''''''
import pickle

update_record = []
roll_update = int(input("Enter the roll no."))

with open("students.dat", "rb") as file:
    try:
        while True:
            record = pickle.load(file)
            if record["roll"] == roll_update:
                record["name"] = input("Enter the name")
                record["marks"] = float(input("Enter the marks"))
                updated_record.append(record)
    except EOFError:
        pass
with open("student.dat", "wb") as file:
    for record in update_record:
        pickle.dump(record.file)
print("Record updated successfully")
'''