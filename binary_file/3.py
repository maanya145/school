#Search the record by roll number
import pickle
roll_search = int(input("Enter the roll number to search: "))
print("Record updated successfully")

#Update the record in binary file
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



