import csv

filename = "students.csv"

# Ensure the file exists with headers
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Class", "Marks"])


# Function to add multiple records
def add_record():
    n = int(input("How many records do you want to add? "))
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        for i in range(n):
            print("\nEnter details for student", i + 1)
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            cls = input("Enter Class: ")
            marks = input("Enter Marks: ")
            writer.writerow([roll, name, cls, marks])
    print(f"\n{n} record(s) added successfully!\n")


# Function to display all records
def display_records():
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()


# Function to search a record by name
def search_record():
    name = input("Enter name to search: ").lower()
    found = False
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == name:
                print("Record found:", row)
                found = True
                break
    if not found:
        print("Record not found.\n")


# Function to delete a record by Roll No
def delete_record():
    roll_to_delete = input("Enter Roll No to delete: ")
    updated_rows = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] != roll_to_delete:
                updated_rows.append(row)

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

    print(f"\nRecord with Roll No {roll_to_delete} deleted (if it existed).\n")


# Menu loop
while True:
    print("=== Student Records Menu ===")
    print("1. Add Records")
    print("2. Display All Records")
    print("3. Search Record by Name")
    print("4. Delete Record by Roll No")
    print("5. Exit")
     
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_record()
    elif choice == "2":
        display_records()
    elif choice == "3":
        search_record()
    elif choice == "4":
        delete_record()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
